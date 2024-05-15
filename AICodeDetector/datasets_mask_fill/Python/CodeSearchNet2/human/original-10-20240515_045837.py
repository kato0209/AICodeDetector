
        client = self.get_conn()
        product_set = self.product_set_name_determiner.get_entity_with_name(
            product_set, product_set_id, location, project_id
        )
        self.log.info('Updating ProductSet: %s', product_set.name)
        response = client.update_product_set(
            product_set=product_set, update_mask=update_mask, retry=retry, timeout=timeout, metadata=metadata
        )
        self.log.info('ProductSet updated: %s', response.name if response else '')
        self.log.debug('ProductSet updated:\n%s', response)
        return MessageToDict(response)