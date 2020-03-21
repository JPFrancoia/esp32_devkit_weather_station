import framebuf

fb_thermometer = framebuf.FrameBuffer(bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00?\xc0\x00\x00\x00\x00\x00\x00\x7f\xe0\x00\x00\x00\x00\x00\x00\xff\xf0\x00\x00\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00\x00\x01\xf0\xf8\x00\x00\x00\x00\x00\x01\xe0x\x00\x00\x00\x00\x00\x01\xe0x\x00\x00\x00\x00\x00\x01\xe0x\x00\x00\x00\x00\x00\x01\xe0x\x00\x00\x00\x00\x00\x01\xe0x\x00\x00\x00\x00\x00\x01\xe0x\x00\x00\x00\x00\x00\x01\xe0x\x00\x00\x00\x00\x00\x01\xe0x\x00\x00\x00\x00\x00\x01\xe0x\x00\x00\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00\x00\x03\xff\xfc\x00\x00\x00\x00\x00\x07\xff\xfe\x00\x00\x00\x00\x00\x0f\xff\xff\x00\x00\x00\x00\x00\x1f\xff\xff\x80\x00\x00\x00\x00\x1f\xff\xff\x80\x00\x00\x00\x00?\xff\xff\x80\x00\x00\x00\x00?\xff\xff\xc0\x00\x00\x00\x00?\xff\xff\xc0\x00\x00\x00\x00?\xff\xff\xc0\x00\x00\x00\x00?\xff\xff\xc0\x00\x00\x00\x00?\xff\xff\xc0\x00\x00\x00\x00?\xff\xff\xc0\x00\x00\x00\x00?\xff\xff\xc0\x00\x00\x00\x00?\xff\xff\xc0\x00\x00\x00\x00\x1f\xff\xff\x80\x00\x00\x00\x00\x1f\xff\xff\x80\x00\x00\x00\x00\x0f\xff\xff\x00\x00\x00\x00\x00\x07\xff\xfe\x00\x00\x00\x00\x00\x03\xff\xfc\x00\x00\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00\x00\x00\x7f\xe0\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 60, 60, framebuf.MONO_HLSB)

fb_humidity = framebuf.FrameBuffer(bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x1f\x80\x00\x00\x00\x00\x00\x00?\xc0\x00\x00\x00\x00\x00\x00\x7f\xe0\x00\x00\x00\x00\x00\x00\x7f\xf0\x00\x00\x00\x00\x00\x00\xff\xf0\x00\x00\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00\x00\x03\xff\xfc\x00\x00\x00\x00\x00\x03\xff\xfc\x00\x00\x00\x00\x00\x07\xff\xfe\x00\x00\x00\x00\x00\x0f\xff\xff\x00\x00\x00\x00\x00\x0f\xff\xff\x00\x00\x00\x00\x00\x1f\xff\xff\x80\x00\x00\x00\x00\x1f\xff\xff\x80\x00\x00\x00\x00<?\xe7\xc0\x00\x00\x00\x008\x1f\xc3\xc0\x00\x00\x00\x00x\x0f\x81\xe0\x00\x00\x00\x00x\x0f\x03\xe0\x00\x00\x00\x00\xf8\x1e\x07\xf0\x00\x00\x00\x00\xfc\x1c\x0f\xf0\x00\x00\x00\x00\xffx\x1f\xf0\x00\x00\x00\x00\xff\xf0?\xf0\x00\x00\x00\x01\xff\xe0\x7f\xf8\x00\x00\x00\x01\xff\xc0\xff\xf8\x00\x00\x00\x01\xff\x81\xff\xf8\x00\x00\x00\x01\xff\x03\xc7\xf8\x00\x00\x00\x00\xfe\x07\x83\xf0\x00\x00\x00\x00\xfc\x0f\x01\xf0\x00\x00\x00\x00\xf8\x1f\x01\xf0\x00\x00\x00\x00\xf8?\x01\xf0\x00\x00\x00\x00|\x7f\x83\xe0\x00\x00\x00\x00~\xff\xc7\xe0\x00\x00\x00\x00?\xff\xff\xc0\x00\x00\x00\x00\x1f\xff\xff\x80\x00\x00\x00\x00\x0f\xff\xff\x00\x00\x00\x00\x00\x07\xff\xfe\x00\x00\x00\x00\x00\x03\xff\xfc\x00\x00\x00\x00\x00\x00\xff\xf0\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 60, 60, framebuf.MONO_HLSB)

fb_pressure = framebuf.FrameBuffer(bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x80\x00\x00\x00\x00\x00\x03\xff\xfc\x00\x00\x00\x00\x00\x0f\xff\xff\x00\x00\x00\x00\x00?\xff\xff\xc0\x00\x00\x00\x00\xff\xff\xff\xf0\x00\x00\x00\x01\xff\x00\x0f\xf8\x00\x00\x00\x03\xfc\x00\x03\xfc\x00\x00\x00\x07\xf0\x00\x00\xfe\x00\x00\x00\x0f\xc0\x00\x00?\x00\x00\x00\x1f\x80\x00\x00\x1f\x80\x00\x00?\x00\xc00\x0f\xc0\x00\x00~\x01\xe0x\x07\xe0\x00\x00|\x01\xe0x\x03\xe0\x00\x00\xf8\x01\xe0\xf8\x01\xf0\x00\x00\xf8\x00\xc0\xf8\x01\xf0\x00\x01\xf0\x00\x01\xf0\x00\xf8\x00\x01\xf0\x00\x01\xf0\x00\xf8\x00\x03\xe0\x00\x01\xe0\x00|\x00\x03\xe0\xe0\x03\xe0p|\x00\x03\xc1\xf0\x03\xe0\xf8<\x00\x03\xc1\xf0\x07\xc0\xf8<\x00\x03\xc0\xe0\x1f\xc0p<\x00\x07\xc0\x00?\xc0\x00>\x00\x07\xc0\x00?\xc0\x00>\x00\x07\xc0\x00\x7f\xe0\x00>\x00\x07\xc0\x00\x7f\xe0\x00>\x00\x07\xc0\x00?\xc0\x00>\x00\x07\xc0\x00?\xc0\x00>\x00\x03\xc0\x00\x1f\x80\x00<\x00\x03\xc0\x00\x06\x00\x00<\x00\x03\xc0\x00\x00\x00\x00<\x00\x03\xe0\x00\x00\x00\x00|\x00\x03\xe0\x00\x00\x00\x00|\x00\x01\xf0\x00\x00\x00\x00\xf8\x00\x01\xf0\x00\x00\x00\x00\xf8\x00\x00\xf8\x00\x1f\x80\x01\xf0\x00\x00\xf8\x01\xff\xf8\x01\xf0\x00\x00|\x07\xff\xfe\x03\xe0\x00\x00~\x1f\xff\xff\x87\xe0\x00\x00??\xff\xff\xcf\xc0\x00\x00\x1f\xff\xff\xff\xff\x80\x00\x00\x0f\xff\xff\xff\xff\x00\x00\x00\x07\xff\xff\xff\xfe\x00\x00\x00\x03\xff\xff\xff\xfc\x00\x00\x00\x01\xff\xff\xff\xf8\x00\x00\x00\x00\xff\xff\xff\xf0\x00\x00\x00\x00?\xff\xff\xc0\x00\x00\x00\x00\x0f\xff\xff\x00\x00\x00\x00\x00\x03\xff\xfc\x00\x00\x00\x00\x00\x00\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 60, 60, framebuf.MONO_HLSB)

fb_light = framebuf.FrameBuffer(bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x1f\x80\x00\x00\x00\x00\x00\x00?\xc0\x00\x00\x00\x00\x00\x00\x7f\xe0\x00\x00\x00\x00\x00\x00\xff\xf0\x00\x00\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00?\xff\xff\xff\xff\xc0\x00\x00?\xff\xff\xff\xff\xc0\x00\x00?\xff\xff\xff\xff\xc0\x00\x00?\xff\xff\xff\xff\xc0\x00\x00?\xff\xff\xff\xff\xc0\x00\x00?\xff\xfc\x1f\xff\xc0\x00\x00?\xff\xfc\x07\xff\xc0\x00\x00?\xff\xfc\x01\xff\xc0\x00\x00?\xff\xfc\x00\xff\xc0\x00\x00?\xff\xfc\x00\x7f\xc0\x00\x00?\xff\xfc\x00?\xc0\x00\x00?\xff\xfc\x00\x1f\xc0\x00\x00?\xff\xfc\x00\x1f\xc0\x00\x00\x7f\xff\xfc\x00\x0f\xe0\x00\x00\xff\xff\xfc\x00\x0f\xf0\x00\x01\xff\xff\xfc\x00\x07\xf8\x00\x03\xff\xff\xfc\x00\x07\xfc\x00\x07\xff\xff\xfc\x00\x07\xfe\x00\x0f\xff\xff\xfc\x00\x07\xff\x00\x1f\xff\xff\xfc\x00\x07\xff\x80\x1f\xff\xff\xfc\x00\x07\xff\x80\x0f\xff\xff\xfc\x00\x07\xff\x00\x07\xff\xff\xfc\x00\x07\xfe\x00\x03\xff\xff\xfc\x00\x07\xfc\x00\x01\xff\xff\xfc\x00\x07\xf8\x00\x00\xff\xff\xfc\x00\x0f\xf0\x00\x00\x7f\xff\xfc\x00\x0f\xe0\x00\x00?\xff\xfc\x00\x1f\xc0\x00\x00?\xff\xfc\x00\x1f\xc0\x00\x00?\xff\xfc\x00?\xc0\x00\x00?\xff\xfc\x00\x7f\xc0\x00\x00?\xff\xfc\x00\xff\xc0\x00\x00?\xff\xfc\x01\xff\xc0\x00\x00?\xff\xfc\x07\xff\xc0\x00\x00?\xff\xfc\x1f\xff\xc0\x00\x00?\xff\xff\xff\xff\xc0\x00\x00?\xff\xff\xff\xff\xc0\x00\x00?\xff\xff\xff\xff\xc0\x00\x00?\xff\xff\xff\xff\xc0\x00\x00?\xff\xff\xff\xff\xc0\x00\x00\x00\x01\xff\xf8\x00\x00\x00\x00\x00\x00\xff\xf0\x00\x00\x00\x00\x00\x00\x7f\xe0\x00\x00\x00\x00\x00\x00?\xc0\x00\x00\x00\x00\x00\x00\x1f\x80\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 60, 60, framebuf.MONO_HLSB)
