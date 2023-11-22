import CHRoco2 as cr2


class PrecitecCHRoco2:
    def __init__(self):
        self.handle = None
        self.ticket = 0

    def open_connection(self, connection_string, device_type=1):
        self.handle = cr2.open_connection(connection_string, device_type)

    def close_connection(self):
        cr2.close_connection(self.handle)
        self.handle = None

    def get_auto_intensity(self):
        return cr2.get_auto_intensity(self.handle)

    def set_auto_intensity(self, value):
        cr2.set_auto_intensity(self.handle, 1, value, self.ticket)

    def get_averaging_factor(self):
        return cr2.get_averaging_factor(self.handle)

    def set_averaging_factor(self, value):
        cr2.set_averaging_factor(self.handle, value, self.ticket)

    def get_scan_rate(self):
        return cr2.get_scan_rate(self.handle)

    def set_scan_rate(self, value):
        cr2.set_scan_rate(self.handle, value, self.ticket)

    def get_full_scale(self):
        return cr2.get_full_scale(self.handle)

    def start_data_streaming(self):
        cr2.start_data_streaming(self.handle, self.ticket)

    def stop_data_streaming(self):
        cr2.stop_data_streaming(self.handle, self.ticket)

    def start_connection_streaming(self):
        cr2.start_connection_streaming(self.handle)

    def stop_connection_streaming(self):
        cr2.stop_connection_streaming(self.handle)

    def set_connection_output_signals(self, signals=None):
        if signals is None:
            signals = [256, 257, 82]
        cr2.set_connection_output_signals(self.handle, signals)

    def get_connection_output_signals(self):
        return cr2.get_connection_output_signals(self.handle)

    def set_detection_window(self, win_from, win_to):
        return cr2.set_detection_window(self.handle, win_from, win_to)

    def get_detection_window(self):
        return cr2.get_detection_window(self.handle)

    def disable_detection_window(self):
        return cr2.disable_detection_window(self.handle)

    def is_detection_window_active(self):
        return cr2.is_detection_window_active(self.handle)

    def flush_buffer(self):
        if self.handle is not None:
            cr2.flush_buffer(self.handle)

    @staticmethod
    def version():
        return cr2.version()

    def get_samples(self, num_samples):
        return cr2.get_samples(self.handle, num_samples)

    def get_last_sample(self):
        return cr2.get_last_sample(self.handle)


def print_status(device_ctrl):
    scr = device_ctrl.get_scan_rate()
    aut = device_ctrl.get_auto_intensity()
    avg = device_ctrl.get_averaging_factor()
    print(f"Scan rate: {scr}\nAverage: {avg}\nAuto: {aut[0]} intens: {aut[1]}")
    out_channels = device_ctrl.get_connection_output_signals()
    print(out_channels)
    dtw = device_ctrl.get_detection_window()
    print(f"Detection Windows: {dtw}")


def configure(pcr2):
    pcr2.set_auto_intensity(40.0)
    pcr2.set_scan_rate(2000)        # in Hertz
    pcr2.set_averaging_factor(10)   # take average of n measurements, ! lowers data rate to scan_rate/n
    pcr2.set_connection_output_signals()
    pcr2.set_detection_window(15.0, 1500.0)

"""
if __name__ == '__main__':
    import time
    croc2 = PrecitecCHRoco2()
    v = croc2.version()
    print('c++ extension version {} loaded'.format(v))
    try:
        croc2.open_connection("192.168.253.2")
    except cr2.Chr2Exception as err:
        print(err)
        exit(0)


    print('connected')
    croc2.stop_data_streaming()
    configure(croc2)
    croc2.start_data_streaming()
    time.sleep(1)
    data = []
    print_status(croc2)
    for n in range(20):
        sample = croc2.get_last_sample()
        data.append(sample)
        time.sleep(0.1)

    for sample in data:
        print("gap: {}µm, quality: {}, intensity: {}".format(*sample))

    croc2.stop_data_streaming()
    croc2.close_connection()
    print('disconnected')
"""










