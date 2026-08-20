# --- helpers.py -----------------------------------------------------------

import numpy as np

def centers_to_vertical_faces(A):
    """
    Map a 2D field defined at cell centers (Nz-1, Nx-1)
    to vertical face centers (Nz-1, Nx).
    """
    Nz1, Nx1 = A.shape
    F = np.empty((Nz1, Nx1+1), dtype=A.dtype)
    F[:, 1:-1] = 0.5 * (A[:, :-1] + A[:, 1:])
    F[:, 0]    = A[:, 0]     # first-order at domain boundary
    F[:, -1]   = A[:, -1]
    return F   # (Nz-1, Nx)

def vertical_faces_to_centers(F):
    """
    Map a field from vertical face centers → cell centers.

    Parameters
    ----------
    F : 2D array (Nz-1, Nx)
        Quantity defined on vertical faces.

    Returns
    -------
    A : 2D array (Nz-1, Nx-1)
        Quantity mapped to cell centers (average between adjacent faces).
    """
    # Average between left and right faces for each cell
    A = 0.5 * (F[:, :-1] + F[:, 1:])
    return A

def vertices_to_horizontal_faces(tau_zx_grid):
    """
    Map a 2D shear stress field τ_zx defined at grid vertices (Nz, Nx)
    to horizontal face centers (Nz, Nx-1).

    Each horizontal face center lies midway between two adjacent
    vertices in the x-direction.

    Parameters
    ----------
    tau_zx_grid : 2D array (Nz, Nx)
        Shear stress τ_zx at grid vertices (Pa).

    Returns
    -------
    sxz_face : 2D array (Nz, Nx-1)
        Shear stress τ_zx mapped to horizontal face centers (Pa).
        Shape is (Nz, Nx-1).
    """
    sxz_face = 0.5 * (tau_zx_grid[:, :-1] + tau_zx_grid[:, 1:])
    return sxz_face

def vertices_to_vertical_faces(tau_vertex):
    """
    Map vertex-based shear stress τ_zx (Nz, Nx) to vertical face centers (Nz-1, Nx).
    Each vertical face value is averaged between the two vertices above and below.

    Parameters
    ----------
    tau_vertex : ndarray (Nz, Nx)
        Shear stress τ_zx (stored at grid vertices).

    Returns
    -------
    tau_face : ndarray (Nz-1, Nx)
        τ_zx mapped to vertical face centers.
    """
    return 0.5 * (tau_vertex[:-1, :] + tau_vertex[1:, :])

def residual_divergence_column(i_cell, sig_xx_grid, tau_zx_grid, vzpts, dx, dz):
    """Discrete divergence residual for a single column."""
    sxx_face = centers_to_vertical_faces(sig_xx_grid)          # (Nz-1, Nx)
    d_sxx_dx = (sxx_face[:, i_cell+1] - sxx_face[:, i_cell]) / dx

    sxz_face = 0.5 * (tau_zx_grid[:, i_cell] + tau_zx_grid[:, i_cell+1])
    d_sxz_dz = np.diff(sxz_face) / dz

    residual_z = d_sxx_dx + d_sxz_dz
    cum_int = np.cumsum(residual_z * dz)
    zcuts = vzpts[1:]
    return zcuts, cum_int



def residual_divergence_grid(sig_xx_grid, tau_zx_grid, vzpts, dx, dz):
    """Vectorised discrete divergence residual (identical behaviour to column-wise)."""
    sxx_face = centers_to_vertical_faces(sig_xx_grid)               # (Nz-1, Nx)
    d_sxx_dx = (sxx_face[:, 1:] - sxx_face[:, :-1]) / dx            # (Nz-1, Nx-1)

    sxz_face = 0.5 * (tau_zx_grid[:, :-1] + tau_zx_grid[:, 1:])     # (Nz, Nx-1)
    d_sxz_dz = (sxz_face[1:, :] - sxz_face[:-1, :]) / dz            # (Nz-1, Nx-1)

    R_div = d_sxx_dx + d_sxz_dz                                     # (Nz-1, Nx-1)
    R_cum = np.cumsum(R_div * dz, axis=0)                           # (Nz-1, Nx-1)
    zcuts = vzpts[1:]
    return zcuts, R_cum
    
def horizontal_index(xpos, vxpts):
    """
    Return the element (cell) index j such that xpos lies within [vxpts[j], vxpts[j+1]).
    If xpos lies exactly on a vertex, return the upper cell index.

    Parameters
    ----------
    xpos : float
        Target x-coordinate (m).
    vxpts : 1D array (Nx)
        Vertex x-coordinates (m).

    Returns
    -------
    j : int
        Cell index (0..Nx-2).
    """
    if xpos <= vxpts[0]:
        return 0
    elif xpos >= vxpts[-1]:
        return len(vxpts) - 2
    else:
        return int(np.searchsorted(vxpts, xpos, side="right") - 1)


def vertical_index(zpos, vzpts):
    """
    Return the element (cell) index i such that zpos lies within [vzpts[i], vzpts[i+1]).
    If zpos lies exactly on a vertex, return the upper cell index.

    Parameters
    ----------
    zpos : float
        Target z-coordinate (m).
    vzpts : 1D array (Nz)
        Vertex z-coordinates (m).

    Returns
    -------
    i : int
        Cell index (0..Nz-2).
    """
    if zpos <= vzpts[0]:
        return 0
    elif zpos >= vzpts[-1]:
        return len(vzpts) - 2
    else:
        return int(np.searchsorted(vzpts, zpos, side="right") - 1)