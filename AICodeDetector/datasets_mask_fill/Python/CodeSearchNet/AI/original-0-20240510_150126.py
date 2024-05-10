_conn_id')
            hook.run(
                hook_name='http_hook',
                http_conn_id='my_conn_id',
                retry_args={'num_retries': 3}
            )

        :param _retry_args: Arguments which define the retry behaviour.
            See Tenacity documentation at https://github.com/jd/tenacity
        :type _retry_args: dict


        :Example::

     