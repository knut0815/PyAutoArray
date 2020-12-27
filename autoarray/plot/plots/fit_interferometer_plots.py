from autoarray.plot.plotter import plotter, include as inc
import numpy as np


@inc.set_include
@plotter.set_plotter_for_subplot
@plotter.set_subplot_filename
def subplot_fit_interferometer(fit, include=None, plotter=None):

    number_subplots = 6

    plotter.open_subplot_figure(number_subplots=number_subplots)

    plotter.setup_subplot(number_subplots=number_subplots, subplot_index=1)

    residual_map_vs_uv_distances(fit=fit, include=include, plotter=plotter)

    plotter.setup_subplot(number_subplots=number_subplots, subplot_index=2)

    normalized_residual_map_vs_uv_distances(fit=fit, include=include, plotter=plotter)

    plotter.setup_subplot(number_subplots=number_subplots, subplot_index=3)

    chi_squared_map_vs_uv_distances(fit=fit, include=include, plotter=plotter)

    plotter.setup_subplot(number_subplots=number_subplots, subplot_index=4)

    residual_map_vs_uv_distances(
        fit=fit, plot_real=False, include=include, plotter=plotter
    )

    plotter.setup_subplot(number_subplots=number_subplots, subplot_index=5)

    normalized_residual_map_vs_uv_distances(
        fit=fit, plot_real=False, include=include, plotter=plotter
    )

    plotter.setup_subplot(number_subplots=number_subplots, subplot_index=6)

    chi_squared_map_vs_uv_distances(
        fit=fit, plot_real=False, include=include, plotter=plotter
    )

    plotter.output.subplot_to_figure()

    plotter.figure.close()


def individuals(
    fit,
    plot_visibilities=False,
    plot_noise_map=False,
    plot_signal_to_noise_map=False,
    plot_model_visibilities=False,
    plot_residual_map=False,
    plot_normalized_residual_map=False,
    plot_chi_squared_map=False,
    include=None,
    plotter=None,
):
    """Plot the model datas_ of an analysis, using the *Fitter* class object.

    The visualization and output type can be fully customized.

    Parameters
    -----------
    fit : autolens.lens.fitting.Fitter
        Class containing fit between the model datas_ and observed lens datas_ (including residual_map, chi_squared_map etc.)
    output_path : str
        The path where the datas_ is output if the output_type is a file format (e.g. png, fits)
    output_format : str
        How the datas_ is output. File formats (e.g. png, fits) output the datas_ to harddisk. 'show' displays the datas_ \
        in the python interpreter window.
    """

    if plot_visibilities:

        visibilities(fit=fit, include=include, plotter=plotter)

    if plot_noise_map:

        noise_map(fit=fit, include=include, plotter=plotter)

    if plot_signal_to_noise_map:

        signal_to_noise_map(fit=fit, include=include, plotter=plotter)

    if plot_model_visibilities:

        model_visibilities(fit=fit, include=include, plotter=plotter)

    if plot_residual_map:

        residual_map_vs_uv_distances(
            fit=fit, plot_real=True, include=include, plotter=plotter
        )

        residual_map_vs_uv_distances(
            fit=fit, plot_real=False, include=include, plotter=plotter
        )

    if plot_normalized_residual_map:

        normalized_residual_map_vs_uv_distances(
            fit=fit, plot_real=True, include=include, plotter=plotter
        )

        normalized_residual_map_vs_uv_distances(
            fit=fit, plot_real=False, include=include, plotter=plotter
        )

    if plot_chi_squared_map:

        chi_squared_map_vs_uv_distances(
            fit=fit, plot_real=True, include=include, plotter=plotter
        )

        chi_squared_map_vs_uv_distances(
            fit=fit, plot_real=False, include=include, plotter=plotter
        )


@inc.set_include
@plotter.set_plotter_for_figure
@plotter.set_labels
def visibilities(fit, include=None, plotter=None):
    """Plot the visibilities of a lens fit.

    Set *autolens.datas.grid.plotter.plotter* for a description of all input parameters not described below.

    Parameters
    -----------
    visibilities : datas.imaging.datas.Imaging
        The datas-datas, which include the observed datas, noise_map, PSF, signal-to-noise_map, etc.
    origin : True
        If true, the origin of the datas's coordinate system is plotted as a 'x'.
    """
    plotter.plot_grid(grid=fit.visibilities.in_grid)


@inc.set_include
@plotter.set_plotter_for_figure
@plotter.set_labels
def noise_map(fit, include=None, plotter=None):
    """Plot the noise-map of a lens fit.

    Set *autolens.datas.grid.plotter.plotter* for a description of all input parameters not described below.

    Parameters
    -----------
    visibilities : datas.imaging.datas.Imaging
        The datas-datas, which include the observed datas, noise_map, PSF, signal-to-noise_map, etc.
    origin : True
        If true, the origin of the datas's coordinate system is plotted as a 'x'.
    """
    plotter.plot_grid(grid=fit.visibilities.in_grid, color_array=np.real(fit.noise_map))


@inc.set_include
@plotter.set_plotter_for_figure
@plotter.set_labels
def signal_to_noise_map(fit, include=None, plotter=None):
    """Plot the noise-map of a lens fit.

    Set *autolens.datas.grid.plotter.plotter* for a description of all input parameters not described below.

    Parameters
    -----------
    visibilities : datas.imaging.datas.Imaging
    The datas-datas, which include the observed datas, signal_to_noise_map, PSF, signal-to-signal_to_noise_map, etc.
    origin : True
    If true, the origin of the datas's coordinate system is plotted as a 'x'.
    """
    plotter.plot_grid(
        grid=fit.visibilities.in_grid, color_array=fit.signal_to_noise_map.real
    )


@inc.set_include
@plotter.set_plotter_for_figure
@plotter.set_labels
def model_visibilities(fit, include=None, plotter=None):
    """Plot the model visibilities of a fit.

    Set *autolens.datas.grid.plotter.plotter* for a description of all input parameters not described below.

    Parameters
    -----------
    fit : datas.fitting.fitting.AbstractFitter
        The fit to the datas, which include a list of every model visibilities, residual_map, chi-squareds, etc.
    visibilities_index : int
        The index of the datas in the datas-set of which the model visibilities is plotted.
    """
    plotter.plot_grid(grid=fit.visibilities.in_grid)


@inc.set_include
@plotter.set_plotter_for_figure
@plotter.set_labels
def residual_map_vs_uv_distances(
    fit,
    plot_real=True,
    label_yunits="V$_{R,data}$ - V$_{R,model}$",
    label_xunits=r"UV$_{distance}$ (k$\lambda$)",
    include=None,
    plotter=None,
):
    """Plot the residual-map of a lens fit.

    Set *autolens.datas.grid.plotter.plotter* for a description of all input parameters not described below.

    Parameters
    -----------
    fit : datas.fitting.fitting.AbstractFitter
        The fit to the datas, which include a list of every model visibilities, residual_map, chi-squareds, etc.
    visibilities_index : int
        The index of the datas in the datas-set of which the residual_map are plotted.
    """

    if plot_real:
        y = np.real(fit.residual_map)
        plotter = plotter.plotter_with_new_labels(
            title_label=f"{plotter.title.kwargs['label']} Real"
        )
        plotter = plotter.plotter_with_new_output(
            filename=plotter.output.filename + "_real"
        )
    else:
        y = np.imag(fit.residual_map)
        plotter = plotter.plotter_with_new_labels(
            title_label=f"{plotter.title.kwargs['label']} Imag"
        )
        plotter = plotter.plotter_with_new_output(
            filename=plotter.output.filename + "_imag"
        )

    plotter.plot_line(
        y=y,
        x=fit.masked_interferometer.interferometer.uv_distances / 10 ** 3.0,
        plot_axis_type="scatter",
    )


@inc.set_include
@plotter.set_plotter_for_figure
@plotter.set_labels
def normalized_residual_map_vs_uv_distances(
    fit,
    plot_real=True,
    label_yunits="V$_{R,data}$ - V$_{R,model}$",
    label_xunits=r"UV$_{distance}$ (k$\lambda$)",
    include=None,
    plotter=None,
):
    """Plot the residual-map of a lens fit.

    Set *autolens.datas.grid.plotter.plotter* for a description of all input parameters not described below.

    Parameters
    -----------
    fit : datas.fitting.fitting.AbstractFitter
        The fit to the datas, which include a list of every model visibilities, residual_map, chi-squareds, etc.
    visibilities_index : int
        The index of the datas in the datas-set of which the residual_map are plotted.
    """

    if plot_real:
        y = np.real(fit.residual_map)
        plotter = plotter.plotter_with_new_labels(
            title_label=f"{plotter.title.kwargs['label']} Real"
        )
        plotter = plotter.plotter_with_new_output(
            filename=plotter.output.filename + "_real"
        )
    else:
        y = np.imag(fit.residual_map)
        plotter = plotter.plotter_with_new_labels(
            title_label=f"{plotter.title.kwargs['label']} Imag"
        )
        plotter = plotter.plotter_with_new_output(
            filename=plotter.output.filename + "_imag"
        )

    plotter.plot_line(
        y=y,
        x=fit.masked_interferometer.interferometer.uv_distances / 10 ** 3.0,
        plot_axis_type="scatter",
    )


@inc.set_include
@plotter.set_plotter_for_figure
@plotter.set_labels
def chi_squared_map_vs_uv_distances(
    fit,
    plot_real=True,
    label_yunits="V$_{R,data}$ - V$_{R,model}$",
    label_xunits=r"UV$_{distance}$ (k$\lambda$)",
    include=None,
    plotter=None,
):
    """Plot the residual-map of a lens fit.

    Set *autolens.datas.grid.plotter.plotter* for a description of all input parameters not described below.

    Parameters
    -----------
    fit : datas.fitting.fitting.AbstractFitter
        The fit to the datas, which include a list of every model visibilities, residual_map, chi-squareds, etc.
    visibilities_index : int
        The index of the datas in the datas-set of which the residual_map are plotted.
    """

    if plot_real:
        y = np.real(fit.residual_map)
        plotter = plotter.plotter_with_new_labels(
            title_label=f"{plotter.title.kwargs['label']} Real"
        )
        plotter = plotter.plotter_with_new_output(
            filename=plotter.output.filename + "_real"
        )
    else:
        y = np.imag(fit.residual_map)
        plotter = plotter.plotter_with_new_labels(
            title_label=f"{plotter.title.kwargs['label']} Imag"
        )
        plotter = plotter.plotter_with_new_output(
            filename=plotter.output.filename + "_imag"
        )

    plotter.plot_line(
        y=y,
        x=fit.masked_interferometer.interferometer.uv_distances / 10 ** 3.0,
        plot_axis_type="scatter",
    )