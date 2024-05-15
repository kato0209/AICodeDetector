
        client = self.get_conn()
        product = self.product_name_determiner.get_entity_with_name(product, product_id, location, project_id)
        self.log.info('Updating ProductSet: %s', product.name)
        response = client.update_product(
            product=product, update_mask=update_mask, retry=retry, timeout=timeout, metadata=metadata
        )
        self.log.info('Product updated: %s', response.name if response else '')
        self.log.debug('Product updated:\n%s', response)
        return MessageToDict(response)