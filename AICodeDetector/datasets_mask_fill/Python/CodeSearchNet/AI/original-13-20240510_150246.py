/docs/json_api/v1/objects#Object
            names.
        :type object_name: str
        :param entity: The entity holding the permission, in one of the following forms:
            user-userId, user-email, group-groupId, group-email, domain-domain,
            project-team-projectId, allUsers, allAuthenticatedUsers.
            See: https://cloud.google.com/storage/docs/access-control/lists#AccessControlList
        :type entity: str
        :param role: The access permission for the entity.
            Acceptable values are: