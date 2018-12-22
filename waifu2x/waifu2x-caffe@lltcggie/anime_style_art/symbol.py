import mxnet as mx
data = mx.symbol.Variable(name='data')
data = mx.symbol.pad(data=data, mode='reflect', pad_width=(0, 0, 0, 0, 7, 7, 7, 7))
conv1_layer = mx.symbol.Convolution(name='conv1_layer', data=data, num_filter=32, pad=(0, 0), kernel=(3,3), stride=(1,1), no_bias=False, dilate=(1, 1), num_group=1, layout='NCHW')
conv1_relu_layer = mx.symbol.LeakyReLU(name='conv1_relu_layer', data=conv1_layer, act_type='leaky', slope=0.100000)
conv2_layer = mx.symbol.Convolution(name='conv2_layer', data=conv1_relu_layer, num_filter=32, pad=(0, 0), kernel=(3,3), stride=(1,1), no_bias=False, dilate=(1, 1), num_group=1, layout='NCHW')
conv2_relu_layer = mx.symbol.LeakyReLU(name='conv2_relu_layer', data=conv2_layer, act_type='leaky', slope=0.100000)
conv3_layer = mx.symbol.Convolution(name='conv3_layer', data=conv2_relu_layer, num_filter=64, pad=(0, 0), kernel=(3,3), stride=(1,1), no_bias=False, dilate=(1, 1), num_group=1, layout='NCHW')
conv3_relu_layer = mx.symbol.LeakyReLU(name='conv3_relu_layer', data=conv3_layer, act_type='leaky', slope=0.100000)
conv4_layer = mx.symbol.Convolution(name='conv4_layer', data=conv3_relu_layer, num_filter=64, pad=(0, 0), kernel=(3,3), stride=(1,1), no_bias=False, dilate=(1, 1), num_group=1, layout='NCHW')
conv4_relu_layer = mx.symbol.LeakyReLU(name='conv4_relu_layer', data=conv4_layer, act_type='leaky', slope=0.100000)
conv5_layer = mx.symbol.Convolution(name='conv5_layer', data=conv4_relu_layer, num_filter=128, pad=(0, 0), kernel=(3,3), stride=(1,1), no_bias=False, dilate=(1, 1), num_group=1, layout='NCHW')
conv5_relu_layer = mx.symbol.LeakyReLU(name='conv5_relu_layer', data=conv5_layer, act_type='leaky', slope=0.100000)
conv6_layer = mx.symbol.Convolution(name='conv6_layer', data=conv5_relu_layer, num_filter=128, pad=(0, 0), kernel=(3,3), stride=(1,1), no_bias=False, dilate=(1, 1), num_group=1, layout='NCHW')
conv6_relu_layer = mx.symbol.LeakyReLU(name='conv6_relu_layer', data=conv6_layer, act_type='leaky', slope=0.100000)
conv7_layer = mx.symbol.Convolution(name='conv7_layer', data=conv6_relu_layer, num_filter=1, pad=(0, 0), kernel=(3,3), stride=(1,1), no_bias=False, dilate=(1, 1), num_group=1, layout='NCHW')
