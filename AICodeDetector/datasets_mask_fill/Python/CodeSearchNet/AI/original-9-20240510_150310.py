
        client = self.get_conn()
        product_set_ref = ProductSetReference(
            location=location, product_set=product_set, project_id=project_id
        )
        product_set_ref.update(product_set)
        result = client.create_product_set(
            location=location,
            product_set_id=product_set_id,
            project_id=project_id,
            retry=retry,
            timeout=timeout,
       