import os
import pandas as pd
import h5py
import numpy as np
from scipy.integrate import trapz, cumulative_trapezoid
from scripts.helpers import *


delrho     = 3250
g          = 9.81
s2my       = 3.1436e13
z_c_depth  = 100e3
xmin       = -1600e3
xmax       = 1600e3
zmin       = -20e3
zmax       = 660e3

def process_file(h5_path):
    """Read key metadata from a single HDF5 model output."""
    # Open the selected model output
    h5file = h5py.File(h5_path, 'r')
    # Access global model parameters
    data = h5file['/Model/Params']
    # Extract and convert model time from seconds to Myr
    time = h5file['/Model/Params'][0].astype(int) / s2my
    # Mesh setup and geometric parameters
    Nx  = data[3].astype(int)
    Nz  = data[4].astype(int)
    dx  = np.ceil((xmax - xmin) / (Nx - 1))   # horizontal spacing (m)
    dz  = np.ceil((zmax - zmin) / (Nz - 1))   # vertical spacing (m)
    vxpts = np.linspace(xmin, xmax, Nx)       # x-coordinates of vertices
    vzpts = np.linspace(zmin, zmax, Nz)       # z-coordinates of vertices
    cxpts = 0.5 * (vxpts[1:] + vxpts[:-1])    # x-centers of cells  → length Nx−1
    czpts = 0.5 * (vzpts[1:] + vzpts[:-1])    # z-centers of cells  → length Nz−1
    vbase_indx = vertical_index(z_c_depth, vzpts)
    cbase_indx = vertical_index(z_c_depth, czpts)
    # Topography and trench loc
    try:
        topo_ = np.column_stack((
            h5file["/Topo"]["x_mark"][:],
            h5file["/Topo"]["z_mark"][:]
        ))
    except KeyError:
        topo_ = np.column_stack((
            h5file["/Topo"]["x"][:],
            h5file["/Topo"]["z"][:]
        ))
    
    new_array = np.zeros((topo_.shape[0], 3))
    new_array[:, :2] = topo_
    topo = new_array[np.argsort(new_array[:, 0])]
    tloc = topo[:, 0][np.argmin(topo[:, 1])]
    tindx = np.argmax(cxpts > tloc)
    topo_mesh = np.interp(cxpts, topo[:, 0], topo[:, 1])
    # Configure stresses
    tau_xz_grid = -1 * np.flipud(h5file["/Vertices"]["sxz"][:].reshape(Nz, Nx))
    pressure_grid = np.flipud(h5file["/Centers"]["P"][:].reshape(Nz-1, Nx-1))
    sigma_I_grid = -1 * pressure_grid                         # (Nz-1, Nx-1)
    tau_xx_grid = np.flipud(h5file["/Centers"]["sxxd"][:].reshape(Nz-1, Nx-1))
    tau_zz_grid = -1 * tau_xx_grid
    sig_xx_grid = sigma_I_grid + tau_xx_grid
    sig_zz_grid = sigma_I_grid + tau_zz_grid
    diff_stress_grid = tau_xx_grid - tau_zz_grid
    #temp_grid = np.flipud(h5file["/Centers"]['T'][:].reshape(Nz-1, Nx-1))
    tau_xz_face = vertices_to_horizontal_faces(tau_xz_grid)
    tau_zx_face = vertices_to_vertical_faces(tau_xz_grid)  # (Nz-1, Nx)
    Vx = -1 * trapz(tau_zx_face, dx=dz, axis=0)  # integrate over z, result shape (Nx,)
    Vx = 0.5 * (Vx [:-1] + Vx [1:])
    V_trench =  Vx[tindx]
    dVdx = np.gradient(Vx, dx)
    vtopo = dVdx / (delrho * g)
    window = 500  # search range in km (or adjusted if vxpts in m)
    mask_x = vxpts > tloc
    tau_sum = np.sum(tau_zx_face, axis=0)[mask_x]
    indx = np.argmin(-1 * tau_sum[:window])
    xi_loc = vxpts[mask_x][:window][indx]
    xi_indx = np.argmin(np.abs(vxpts - xi_loc))
    xi_dist = xi_loc - tloc
    trench_relative_topo = (
        topo[:, 1][np.argmin(np.abs(topo[:, 0] - xi_loc))] -
        topo[:, 1][np.argmin(np.abs(topo[:, 0] - tloc))]
    )
    xm_indx = int(tindx + 0.5 * (xi_indx - tindx))
    np_mask = np.logical_and(czpts>10e3, czpts<50e3)
    # Neutral plane extraction
    np_depth = -99
    z_vals = diff_stress_grid[:, xm_indx][np_mask]
    x_vals = czpts[np_mask]
    sign_changes = np.where(np.diff(np.sign(z_vals)))[0]
    if len(sign_changes) > 0:
        idx = sign_changes[0]  # Take the first crossing
        x1, x2 = x_vals[idx], x_vals[idx + 1]
        y1, y2 = z_vals[idx], z_vals[idx + 1]
    
        # Linear interpolation for zero crossing
        np_depth = x1 - y1 * (x2 - x1) / (y2 - y1)
    gpe_est = trench_relative_topo*delrho*g*np_depth
    
    #calculate the vertically integrated quantities
    sig_xx_face = centers_to_vertical_faces(sig_xx_grid)
    bar_sig_xx = np.cumsum(sig_xx_face * dz, axis=0)
    sig_zz_face = centers_to_vertical_faces(sig_zz_grid)
    bar_sig_zz = np.cumsum(sig_zz_face * dz, axis=0)
    diff_stress_face = centers_to_vertical_faces(diff_stress_grid)
    bar_diff_stress = np.cumsum(diff_stress_face * dz, axis=0)
    tau_xz_face = vertices_to_horizontal_faces(tau_xz_grid)
    FB_x_grid = np.cumsum(tau_xz_face  * dx, axis=1)
    #calc the delta quantities
    ref_index = tindx
    del_bar_sig_xx      = bar_sig_xx[:, 1:]      - bar_sig_xx[:, [ref_index]]
    del_bar_sig_zz      = bar_sig_zz[:, 1:]      - bar_sig_zz[:, [ref_index]]
    del_bar_diff_stress = bar_diff_stress[:, 1:] - bar_diff_stress[:, [ref_index]]
    FB_x_grid           = FB_x_grid[:]           - FB_x_grid[:, [ref_index]]
    #make sure this retrurns a finite vlaue
    # Identify the depth (vertical face) index closest to z_c_depth
    zindx = vertical_index(z_c_depth, czpts)
    Fd_trench = bar_diff_stress[zindx, tindx]
    #these are already referenced to zero at trnch
    del_Fd = del_bar_diff_stress[zindx, xi_indx]
    del_gpe = -1*del_bar_sig_zz[zindx, xi_indx]
    

    

    #######
    #Return
    #######
    return {
        "time_Myr": time,
        "trench_loc": tloc,
        "trench_rel_topo": trench_relative_topo,
        "neutral_plane_depth": np_depth,
        "shear_res_trench": 1e-12*V_trench, 
        "trench_gpe_est": 1e-12*gpe_est,
        "Fd_trench": 1e-12*Fd_trench,
        "delta_Fd": 1e-12*del_Fd, 
        "delta_gpe": 1e-12*del_gpe, 
    }




def process_directory(input_dir, output_csv, verbose=True):
    """Loop over all HDF5 files in input_dir and save results to output_csv."""
    results = []
    files = sorted([f for f in os.listdir(input_dir) if f.endswith(".h5")])

    if verbose:
        print(f"🔍 Found {len(files)} HDF5 files in {os.path.abspath(input_dir)}")

    for fname in files:
        fpath = os.path.join(input_dir, fname)
        try:
            res = process_file(fpath)
            results.append(res)
            if verbose:
                print(f"Processed {fname}")
        except Exception as e:
            if verbose:
                print(f"⚠️  Failed on {fname}: {e}")

    if results:
        df = pd.DataFrame(results)
        df.to_csv(output_csv, index=False)
        if verbose:
            print(f"\n✅ Wrote {len(results)} summaries → {output_csv}")
    else:
        if verbose:
            print("No models processed successfully.")

# Example usage:
# process_directory("model_output_data/MD7_ref_model", "stress_summary.csv")