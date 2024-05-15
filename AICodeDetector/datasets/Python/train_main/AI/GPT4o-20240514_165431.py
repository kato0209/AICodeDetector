

        self,
        location,
        product_set,
        project_id=None,
        product_set_id=None,
        retry=Retry(),
        timeout=DEFAULT,
        metadata=None,
    ):
    client = vision_v1.ProductSearchClient()
    
    if project_id is None:
        project_id = client.project
    
    parent = f"projects/{project_id}/locations/{location}"
    
    response = client.create_product_set(
        parent=parent,
       