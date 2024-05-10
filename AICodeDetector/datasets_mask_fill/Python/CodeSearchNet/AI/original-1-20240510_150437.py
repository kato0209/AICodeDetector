

    Examples:
       .. code-block:: python

            import numpy as np
            from PIL import Image
            from torchvision import transforms

            image = np.random.rand(224, 224, 3)
            image = transforms.Normalize(mean=image, std=image, inplace=True)
            image = image.numpy()
            image.shape
           