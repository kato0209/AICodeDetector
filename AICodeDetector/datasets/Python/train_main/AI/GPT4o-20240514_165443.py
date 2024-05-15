
    client = vision_v1.ProductSearchClient()

    if project_id is None:
        project_id = client.project

    product_path = client.product_path(project_id, location, product_id)

    client.delete_product(name=product_path, retry=retry, timeout=timeout, metadata=metadata)
