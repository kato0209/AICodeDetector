

__all__ = ['SqueezeNet', 'squeezenet1_1']

model_urls = {
    'squeezenet1_1': 'https://download.pytorch.org/models/squeezenet1_1-b8a52dc0.pth',
}

class Fire(nn.Module):
        super(Fire, self).__init__()
        self