from autoarray.plot import plotters


@plotters.set_subplot_filename
def subplot_inversion(
    inversion,
    mask=None,
    lines=None,
    positions=None,
    grid=None,
    image_pixel_indexes=None,
    source_pixel_indexes=None,
    include=plotters.Include(),
    sub_plotter=plotters.SubPlotter(),
):

    number_subplots = 6

    ratio = float(
        (
            inversion.mapper.grid.scaled_maxima[1]
            - inversion.mapper.grid.scaled_minima[1]
        )
        / (
            inversion.mapper.grid.scaled_maxima[0]
            - inversion.mapper.grid.scaled_minima[0]
        )
    )

    if sub_plotter.figure.aspect in "square":
        aspect_inv = ratio
    elif sub_plotter.figure.aspect in "auto":
        aspect_inv = 1.0 / ratio
    elif sub_plotter.figure.aspect in "equal":
        aspect_inv = 1.0

    sub_plotter.open_subplot_figure(number_subplots=number_subplots)

    sub_plotter.setup_subplot(number_subplots=number_subplots, subplot_index=1)

    reconstructed_image(
        inversion=inversion,
        mask=mask,
        lines=lines,
        positions=positions,
        grid=grid,
        include=include,
        plotter=sub_plotter,
    )

    sub_plotter.setup_subplot(
        number_subplots=number_subplots, subplot_index=2, aspect=aspect_inv
    )

    reconstruction(
        inversion=inversion,
        positions=None,
        lines=lines,
        include=include,
        plotter=sub_plotter,
        image_pixel_indexes=image_pixel_indexes,
        source_pixel_indexes=source_pixel_indexes,
    )

    sub_plotter.setup_subplot(
        number_subplots=number_subplots, subplot_index=3, aspect=aspect_inv
    )

    errors(
        inversion=inversion,
        positions=None,
        image_pixel_indexes=image_pixel_indexes,
        source_pixel_indexes=source_pixel_indexes,
        include=include,
        plotter=sub_plotter,
    )

    sub_plotter.setup_subplot(
        number_subplots=number_subplots, subplot_index=4, aspect=aspect_inv
    )

    residual_map(
        inversion=inversion,
        positions=None,
        image_pixel_indexes=image_pixel_indexes,
        source_pixel_indexes=source_pixel_indexes,
        include=include,
        plotter=sub_plotter,
    )

    sub_plotter.setup_subplot(
        number_subplots=number_subplots, subplot_index=5, aspect=aspect_inv
    )

    chi_squared_map(
        inversion=inversion,
        positions=None,
        image_pixel_indexes=image_pixel_indexes,
        source_pixel_indexes=source_pixel_indexes,
        include=include,
        plotter=sub_plotter,
    )

    sub_plotter.setup_subplot(
        number_subplots=number_subplots, subplot_index=6, aspect=aspect_inv
    )

    regularization_weights(
        inversion=inversion,
        positions=None,
        image_pixel_indexes=image_pixel_indexes,
        source_pixel_indexes=source_pixel_indexes,
        include=include,
        plotter=sub_plotter,
    )

    sub_plotter.output.subplot_to_figure()

    sub_plotter.figure.close()


def individuals(
    inversion,
    lines=None,
    positions=None,
    plot_reconstructed_image=False,
    plot_reconstruction=False,
    plot_errors=False,
    plot_residual_map=False,
    plot_normalized_residual_map=False,
    plot_chi_squared_map=False,
    plot_regularization_weight_map=False,
    plot_interpolated_reconstruction=False,
    plot_interpolated_errors=False,
    include=plotters.Include(),
    plotter=plotters.Plotter(),
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

    if plot_reconstructed_image:

        reconstructed_image(inversion=inversion, include=include, plotter=plotter)

    if plot_reconstruction:

        reconstruction(
            inversion=inversion,
            positions=positions,
            lines=lines,
            include=include,
            plotter=plotter,
        )

    if plot_errors:

        errors(inversion=inversion, include=include, plotter=plotter)

    if plot_residual_map:

        residual_map(inversion=inversion, include=include, plotter=plotter)

    if plot_normalized_residual_map:

        normalized_residual_map(inversion=inversion, include=include, plotter=plotter)

    if plot_chi_squared_map:

        chi_squared_map(inversion=inversion, include=include, plotter=plotter)

    if plot_regularization_weight_map:

        regularization_weights(inversion=inversion, include=include, plotter=plotter)

    if plot_interpolated_reconstruction:

        interpolated_reconstruction(
            inversion=inversion,
            positions=positions,
            lines=lines,
            include=include,
            plotter=plotter,
        )

    if plot_interpolated_errors:

        interpolated_errors(
            inversion=inversion, lines=lines, include=include, plotter=plotter
        )


@plotters.set_labels
def reconstructed_image(
    inversion,
    mask=None,
    grid=None,
    lines=None,
    positions=None,
    include=plotters.Include(),
    plotter=plotters.Plotter(),
):

    plotter.plot_array(
        array=inversion.mapped_reconstructed_image,
        mask=mask,
        lines=lines,
        positions=positions,
        grid=grid,
        include_origin=include.origin,
    )


@plotters.set_labels
def reconstruction(
    inversion,
    lines=None,
    positions=None,
    image_pixel_indexes=None,
    source_pixel_indexes=None,
    include=plotters.Include(),
    plotter=plotters.Plotter(),
):

    source_pixel_values = inversion.mapper.reconstructed_pixelization_from_solution_vector(
        solution_vector=inversion.reconstruction
    )

    plotter.plot_mapper(
        mapper=inversion.mapper,
        source_pixel_values=source_pixel_values,
        lines=lines,
        positions=positions,
        image_pixel_indexes=image_pixel_indexes,
        source_pixel_indexes=source_pixel_indexes,
        include_origin=include.origin,
        include_pixelization_grid=include.inversion_pixelization_grid,
        include_grid=include.inversion_grid,
        include_border=include.inversion_border,
    )


@plotters.set_labels
def errors(
    inversion,
    positions=None,
    lines=None,
    image_pixel_indexes=None,
    source_pixel_indexes=None,
    include=plotters.Include(),
    plotter=plotters.Plotter(),
):

    source_pixel_values = inversion.mapper.reconstructed_pixelization_from_solution_vector(
        solution_vector=inversion.errors
    )

    plotter.plot_mapper(
        mapper=inversion.mapper,
        source_pixel_values=source_pixel_values,
        lines=lines,
        positions=positions,
        image_pixel_indexes=image_pixel_indexes,
        source_pixel_indexes=source_pixel_indexes,
        include_origin=include.origin,
        include_pixelization_grid=include.inversion_pixelization_grid,
        include_grid=include.inversion_grid,
        include_border=include.inversion_border,
    )


@plotters.set_labels
def residual_map(
    inversion,
    positions=None,
    lines=None,
    image_pixel_indexes=None,
    source_pixel_indexes=None,
    include=plotters.Include(),
    plotter=plotters.Plotter(),
):

    source_pixel_values = inversion.mapper.reconstructed_pixelization_from_solution_vector(
        solution_vector=inversion.residual_map
    )

    plotter.plot_mapper(
        mapper=inversion.mapper,
        source_pixel_values=source_pixel_values,
        lines=lines,
        positions=positions,
        image_pixel_indexes=image_pixel_indexes,
        source_pixel_indexes=source_pixel_indexes,
        include_origin=include.origin,
        include_pixelization_grid=include.inversion_pixelization_grid,
        include_grid=include.inversion_grid,
        include_border=include.inversion_border,
    )


@plotters.set_labels
def normalized_residual_map(
    inversion,
    positions=None,
    lines=None,
    image_pixel_indexes=None,
    source_pixel_indexes=None,
    include=plotters.Include(),
    plotter=plotters.Plotter(),
):

    source_pixel_values = inversion.mapper.reconstructed_pixelization_from_solution_vector(
        solution_vector=inversion.normalized_residual_map
    )

    plotter.plot_mapper(
        mapper=inversion.mapper,
        source_pixel_values=source_pixel_values,
        lines=lines,
        positions=positions,
        image_pixel_indexes=image_pixel_indexes,
        source_pixel_indexes=source_pixel_indexes,
        include_origin=include.origin,
        include_pixelization_grid=include.inversion_pixelization_grid,
        include_grid=include.inversion_grid,
        include_border=include.inversion_border,
    )


@plotters.set_labels
def chi_squared_map(
    inversion,
    positions=None,
    lines=None,
    image_pixel_indexes=None,
    source_pixel_indexes=None,
    include=plotters.Include(),
    plotter=plotters.Plotter(),
):

    source_pixel_values = inversion.mapper.reconstructed_pixelization_from_solution_vector(
        solution_vector=inversion.chi_squared_map
    )

    plotter.plot_mapper(
        mapper=inversion.mapper,
        source_pixel_values=source_pixel_values,
        lines=lines,
        positions=positions,
        image_pixel_indexes=image_pixel_indexes,
        source_pixel_indexes=source_pixel_indexes,
        include_origin=include.origin,
        include_pixelization_grid=include.inversion_pixelization_grid,
        include_grid=include.inversion_grid,
        include_border=include.inversion_border,
    )


@plotters.set_labels
def regularization_weights(
    inversion,
    positions=None,
    lines=None,
    image_pixel_indexes=None,
    source_pixel_indexes=None,
    include=plotters.Include(),
    plotter=plotters.Plotter(),
):

    regularization_weights = inversion.regularization.regularization_weights_from_mapper(
        mapper=inversion.mapper
    )

    plotter.plot_mapper(
        mapper=inversion.mapper,
        source_pixel_values=regularization_weights,
        lines=lines,
        positions=positions,
        image_pixel_indexes=image_pixel_indexes,
        source_pixel_indexes=source_pixel_indexes,
        include_origin=include.origin,
        include_pixelization_grid=include.inversion_pixelization_grid,
        include_grid=include.inversion_grid,
        include_border=include.inversion_border,
    )


@plotters.set_labels
def interpolated_reconstruction(
    inversion,
    lines=None,
    positions=None,
    grid=None,
    include=plotters.Include(),
    plotter=plotters.Plotter(),
):

    plotter.plot_array(
        array=inversion.interpolated_reconstruction_from_shape_2d(),
        lines=lines,
        positions=positions,
        grid=grid,
        include_origin=include.origin,
    )


@plotters.set_labels
def interpolated_errors(
    inversion,
    lines=None,
    positions=None,
    grid=None,
    include=plotters.Include(),
    plotter=plotters.Plotter(),
):

    plotter.plot_array(
        array=inversion.interpolated_errors_from_shape_2d(),
        lines=lines,
        positions=positions,
        grid=grid,
        include_origin=include.origin,
    )
