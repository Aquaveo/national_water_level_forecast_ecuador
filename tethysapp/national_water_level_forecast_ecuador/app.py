from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import CustomSetting, SpatialDatasetServiceSetting

class NationalWaterLevelForecastEcuador(TethysAppBase):
    """
    Tethys app class for National Water Level Forecast Ecuador.
    """

    name = 'National Water Level Forecast Ecuador'
    index = 'national_water_level_forecast_ecuador:home'
    icon = 'national_water_level_forecast_ecuador/images/nwlf.jpg'
    package = 'national_water_level_forecast_ecuador'
    root_url = 'national-water-level-forecast-ecuador'
    color = '#4074dd'
    description = ''
    tags = '"Hydrology", "Time Series", "Bias Correction", "Hydrostats", "GEOGloWS", "Water Level", "Ecuador"'
    enable_feedback = False
    feedback_emails = []

    def spatial_dataset_service_settings(self):
        """
        Spatial_dataset_service_settings method.
        """
        return (
            SpatialDatasetServiceSetting(
                name='main_geoserver',
                description='spatial dataset service for app to use (https://tethys2.byu.edu/geoserver/rest/)',
                engine=SpatialDatasetServiceSetting.GEOSERVER,
                required=True,
            ),
        )

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='national-water-level-forecast-ecuador',
                controller='national_water_level_forecast_ecuador.controllers.home'
            ),
            UrlMap(
                name='get_popup_response',
                url='get-request-data',
                controller='national_water_level_forecast_ecuador.controllers.get_popup_response'
            ),
            UrlMap(
                name='get_hydrographs',
                url='get-hydrographs',
                controller='national_water_level_forecast_ecuador.controllers.get_hydrographs'
            ),
            UrlMap(
                name='get_dailyAverages',
                url='get-dailyAverages',
                controller='national_water_level_forecast_ecuador.controllers.get_dailyAverages'
            ),
            UrlMap(
                name='get_monthlyAverages',
                url='get-monthlyAverages',
                controller='national_water_level_forecast_ecuador.controllers.get_monthlyAverages'
            ),
            UrlMap(
                name='get_scatterPlot',
                url='get-scatterPlot',
                controller='national_water_level_forecast_ecuador.controllers.get_scatterPlot'
            ),
            UrlMap(
                name='get_scatterPlotLogScale',
                url='get-scatterPlotLogScale',
                controller='national_water_level_forecast_ecuador.controllers.get_scatterPlotLogScale'
            ),
            UrlMap(
                name='make_table_ajax',
                url='make-table-ajax',
                controller='national_water_level_forecast_ecuador.controllers.make_table_ajax'
            ),
            UrlMap(
                name='get-available-dates',
                url='ecmwf-rapid/get-available-dates',
                controller='national_water_level_forecast_ecuador.controllers.get_available_dates'
            ),
            UrlMap(
                name='get-time-series-bc',
                url='get-time-series-bc',
                controller='national_water_level_forecast_ecuador.controllers.get_time_series_bc'
            ),
            #UrlMap(
            #    name='get_observed_water_level_csv',
            #    url='get-observed-water-level-csv',
            #    controller='national_water_level_forecast_ecuador.controllers.get_observed_water_level_csv'
            #),
            UrlMap(
                name='get_simulated_bc_water_level_csv',
                url='get-simulated-bc-water-level-csv',
                controller='national_water_level_forecast_ecuador.controllers.get_simulated_bc_water_level_csv'
            ),
            UrlMap(
                name='get_forecast_bc_data_csv',
                url='get-forecast-bc-data-csv',
                controller='national_water_level_forecast_ecuador.controllers.get_forecast_bc_data_csv'
            ),
            UrlMap(
                name='get_forecast_ensemble_bc_data_csv',
                url='get-forecast-ensemble-bc-data-csv',
                controller='national_water_level_forecast_ecuador.controllers.get_forecast_ensemble_bc_data_csv'
            ),
            UrlMap(
                name='user_manual',
                url='national-water-level-forecast-ecuador/user_manual',
                controller='national_water_level_forecast_ecuador.controllers.user_manual'
            ),
            UrlMap(
                name='technical_manual',
                url='national-water-level-forecast-ecuador/technical_manual',
                controller='national_water_level_forecast_ecuador.controllers.technical_manual'
            ),
            ########################################
            ########################################
            UrlMap(
                name="get_zoom_array",
                url="get-zoom-array",
                controller="national_water_level_forecast_ecuador.controllers.get_zoom_array",
            ),
            ########################################
            ########################################
        )

        return url_maps

    def custom_settings(self):
        return (
            CustomSetting(
                name='workspace',
                type=CustomSetting.TYPE_STRING,
                description='Workspace within Geoserver where web service is',
                required=True,
                default='ecuador_hydroviewer',
            ),
            CustomSetting(
                name='region',
                type=CustomSetting.TYPE_STRING,
                description='GESS Region',
                required=True,
                default='south_america-geoglows',
            ),
            CustomSetting(
                name='hydroshare_resource_id',
                type=CustomSetting.TYPE_STRING,
                description='Hydroshare Resource ID',
                required=True,
            ),
            CustomSetting(
                name='username',
                type=CustomSetting.TYPE_STRING,
                description='Hydroshare Username',
                required=True,
            ),
            CustomSetting(
                name='password',
                type=CustomSetting.TYPE_STRING,
                description='Hydroshare Password',
                required=True,
            ),
        )