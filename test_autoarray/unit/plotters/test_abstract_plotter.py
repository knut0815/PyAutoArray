from os import path
import autoarray as aa
from autoarray import conf
from autoarray.plotters import abstract_plotter

import pytest

directory = path.dirname(path.realpath(__file__))

@pytest.fixture(autouse=True)
def set_config_path():
    conf.instance = conf.Config(
        path.join(directory, "../test_files/settings"), path.join(directory, "output")
    )

class TestPlotterArray:

    def test__plotter_settings_use_config_if_not_manually_input(self):

        plotter = abstract_plotter.AbstractPlotter()

        assert plotter.figsize == (7, 7)
        assert plotter.aspect == "square"
        assert plotter.cmap == "jet"
        assert plotter.norm == "linear"
        assert plotter.norm_min == None
        assert plotter.norm_max == None
        assert plotter.linthresh == 0.05
        assert plotter.linscale == 0.1
        assert plotter.cb_ticksize == 10
        assert plotter.cb_fraction == 0.047
        assert plotter.cb_pad == 0.01
        assert plotter.titlesize == 16
        assert plotter.xlabelsize == 16
        assert plotter.ylabelsize == 16
        assert plotter.xyticksize == 16
        assert plotter.mask_pointsize == 10
        assert plotter.border_pointsize == 12
        assert plotter.point_pointsize == 30
        assert plotter.grid_pointsize == 1

        plotter = abstract_plotter.AbstractPlotter(figsize=(6,6), aspect="auto", cmap="cold", norm="log", norm_min=0.1, norm_max=1.0,
                                    linthresh=1.5, linscale=2.0, cb_ticksize=20, cb_fraction=0.001, cb_pad=10.0,
                                    titlesize=20, xlabelsize=21, ylabelsize=22,
                                    xyticksize=23, mask_pointsize=24, border_pointsize=25, point_pointsize=26, grid_pointsize=27)

        assert plotter.figsize == (6, 6)
        assert plotter.aspect == "auto"
        assert plotter.cmap == "cold"
        assert plotter.norm == "log"
        assert plotter.norm_min == 0.1
        assert plotter.norm_max == 1.0
        assert plotter.linthresh == 1.5
        assert plotter.linscale == 2.0
        assert plotter.cb_ticksize == 20
        assert plotter.cb_fraction == 0.001
        assert plotter.cb_pad == 10.0
        assert plotter.titlesize == 20
        assert plotter.xlabelsize == 21
        assert plotter.ylabelsize == 22
        assert plotter.xyticksize == 23
        assert plotter.mask_pointsize == 24
        assert plotter.border_pointsize == 25
        assert plotter.point_pointsize == 26
        assert plotter.grid_pointsize == 27

    def test__plotter_include_use_config_if_not_manually_input(self):

        plotter = abstract_plotter.AbstractPlotter()

        assert plotter.include_origin == True
        assert plotter.include_mask == True
        assert plotter.include_border == False
        assert plotter.include_points == True

        plotter = abstract_plotter.AbstractPlotter(include_origin=False, include_mask=False, include_border=True, include_points=False)

        assert plotter.include_origin == False
        assert plotter.include_mask == False
        assert plotter.include_border == True
        assert plotter.include_points == False

    def test__plotter_manual_labels_are_setup_correctly(self):

        plotter = abstract_plotter.AbstractPlotter()

        assert plotter.label_title == None
        assert plotter.label_yunits == None
        assert plotter.label_xunits == None
        assert plotter.label_yticks == None
        assert plotter.label_xticks == None
        assert plotter.cb_tick_values == None
        assert plotter.cb_tick_labels == None

        plotter = abstract_plotter.AbstractPlotter(label_title="OMG", label_yunits="hi", label_xunits="hi2", label_yticks=[1.0, 2.0], label_xticks=[3.0, 4.0], cb_tick_values=[5.0, 6.0],
                                cb_tick_labels=[7.0, 8.0])

        assert plotter.label_title == "OMG"
        assert plotter.label_yunits == "hi"
        assert plotter.label_xunits == "hi2"
        assert plotter.label_yticks == [1.0, 2.0]
        assert plotter.label_xticks == [3.0, 4.0]
        assert plotter.cb_tick_values == [5.0, 6.0]
        assert plotter.cb_tick_labels == [7.0, 8.0]

    def test__plotter_outputs_are_setup_correctly(self):

        plotter = abstract_plotter.AbstractPlotter()

        assert plotter.output_path == None
        assert plotter.output_format == "show"
        assert plotter.output_filename == None

        plotter = abstract_plotter.AbstractPlotter(output_path="Path", output_format="png", output_filename="file")

        assert plotter.output_path == "Path"
        assert plotter.output_format == "png"
        assert plotter.output_filename == "file"

    def test__plotter_number_of_subplots(self):

        plotter = abstract_plotter.AbstractPlotter()

        rows, columns, figsize = plotter.get_subplot_rows_columns_figsize(number_subplots=1)

        assert rows == 1
        assert columns == 2
        assert figsize == (18, 8)

        rows, columns, figsize = plotter.get_subplot_rows_columns_figsize(number_subplots=4)

        assert rows == 2
        assert columns == 2
        assert figsize == (13, 10)
