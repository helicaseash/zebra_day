def test_printers_config_loading():
    
    from zebra_day import print_mgr as zd

    zd_pm = zd.zpl()

    assert 'labs' in zd_pm.printers.keys()


def test_printers_clear_reset():

    pass
