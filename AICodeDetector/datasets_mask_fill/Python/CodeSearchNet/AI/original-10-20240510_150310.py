
        client = self.get_conn()
        product_set_ref = ProductSetReference(
            location=location, product_set=product_set, project_id=project_id
        )
        result = client.update_product_set(
            product_set=product_set, update_mask=update_mask, retry=retry, timeout=timeout, metadata=metadata
        )
        self.log.info("ProductSet updated.")
        self.log.info("ProductSet ref %s updated to %s", product_set_ref, result.name)
        self.log.info("