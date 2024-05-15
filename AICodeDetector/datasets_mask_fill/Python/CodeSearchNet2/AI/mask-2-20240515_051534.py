
        image_feature = image_feature.resize(self.image_size, Image.ANTIALIAS)
        image_feature = image_feature.convert("RGB")
        image_feature = image_feature.resize((self.image_size, self.image_size), Image.ANTIALIAS)
        image_feature = image_feature.convert("L")
        image_feature = image_feature.resize((self.image_size, self.image_size), Image.ANTIALIAS)
        image_feature = image_feature.convert("RGB")
        image_feature = image_feature