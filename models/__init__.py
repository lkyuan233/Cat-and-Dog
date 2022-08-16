from .wide_resnet import Wide_ResNet

def get_clf(name, num_classes, clf_type='inner', dr=0.0):
    if name == 'wrn40':
        clf = Wide_ResNet(depth=40, widen_factor=4, dropout_rate=dr, num_classes=num_classes, clf_type=clf_type)
    elif name == 'wrn28':
        clf = Wide_ResNet(depth=28, widen_factor=10, dropout_rate=dr, num_classes=num_classes, clf_type=clf_type)
    else:
        raise RuntimeError('---> Invalid CLF name {}'.format(name))
    
    return clf