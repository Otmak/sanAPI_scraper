# O.T onchain

import san
import time

san.ApiConfig.api_key = 'xqc4wlbnq66jav57_ohnds6x5skk33wod'
a = san.available_metrics_for_slug('ethereum')
z = san.get(f'{"circulation"}/{"ethereum"}', interval="5m", include_incomplete_data=True, from_date="utc_now-1h",
            to_date="utc_now")

class Organise:

    def __init__(self, slug):
        self.slug = slug

    def get_list(self):
        metric_list = san.available_metrics_for_slug(self.slug)
        return metric_list

    def get_value(self):
        print('getting value...')
        metric_list = self.get_list()
        print('list', len(metric_list))
        counter = 0

        for metric in metric_list:
            try:
                counter += 1
                call_metric = san.get(f'{metric}/{self.slug}', interval="5m", from_date="utc_now-1h", to_date="utc_now")
                metric_value = call_metric.values[-1][0]
                yield {'metric_name': metric, 'value': metric_value, 'slug': self.slug}
            except Exception as e:
                # ewgex to filter error message
                # print('args', e.args)
                pass

