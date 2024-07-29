
human_codes = [
    """
    def JC69 (mu=1.0, alphabet="nuc", **kwargs):
        num_chars = len(alphabets[alphabet])
        W, pi = np.ones((num_chars,num_chars)), np.ones(num_chars)
        gtr = GTR(alphabet=alphabet)
        gtr.assign_rates(mu=mu, pi=pi, W=W)
        return gt
    """,
    """
    def loop(self, sequences=None, outputs=None, non_sequences=None, block=None, **kwargs):
        from loop import Loop
        return Loop(sequences, outputs, non_sequences, block, **kwargs)
    """,
    """
    def _logsum_expbig_minus_expsmall(big, small):
        with tf.name_scope("logsum_expbig_minus_expsmall"):
            return tf.math.log1p(-tf.exp(small - big)) + big
    """,
    """
    def __openlib(self):
        if self.__getattribute__('_libloaded'):
            return
        libpath_list = self.__get_libres()
        for p in libpath_list:
            try:
                libres = resource_filename(self._module_name, p)
                self.lib = self.ffi.dlopen(libres)
                return
            except:
    """,
    """
    def __coord_cqt_hz(n, fmin=None, bins_per_octave=12, **_kwargs):
        if fmin is None:
            fmin = core.note_to_hz('C1')

        # we drop by half a bin so that CQT bins are centered vertically
        return core.cqt_frequencies(n+1,
                                    fmin=fmin / 2.0**(0.5/bins_per_octave),
                                    bins_per_octave=bins_per_octave
    """,
    """
    def run_samtools_index(job, bam):
        work_dir = job.fileStore.getLocalTempDir()
        job.fileStore.readGlobalFile(bam, os.path.join(work_dir, 'sample.bam'))
        # Call: index the bam
        parameters = ['index', '/data/sample.bam']
        dockerCall(job=job, workDir=work_dir, parameters=parameters,
                tool='quay.io/ucsc_cgl/samtools:0.1.19--dd5ac549b95eb3e5d166a5e310417ef13651994e')
        # Write to fileStore
        return job.fileStore.writeGlobalFile(os.path.join(work_dir, 'sample.bam.bai'))
    """,

    """
    def signature(frame):
        if not frame: return None
        code = frame.f_code
        return (code.co_name, code.co_filename, code.co_firstlineno)
    """,
    """
    import matplotlib.pyplot as plt
    N = len(all_boundaries)  # Number of lists of boundaries
    if algo_ids is None:
        algo_ids = io.get_algo_ids(est_file)

    # Translate ids
    for i, algo_id in enumerate(algo_ids):
        algo_ids[i] = translate_ids[algo_id]
    algo_ids = ["GT"] + algo_ids

    figsize = (6, 4)
    plt.figure(1, figsize=figsize, dpi=120, facecolor='w', edgecolor='k')
    for i, boundaries in enumerate(all_boundaries):
        color = "b"
        if i == 0:
            color =
    """,
    """
    def write_to_file(file_path, content, encoding=None):
    try:
        # TODO: check if in Python2 this should be this way
        # it's possible that we have to make this function more complex
        # to check type(content) and depending on that set 'w' without enconde
        # or 'wb' with encode.
        with open(file_path, "wb") as f:
            f.write(content.encode(encoding))
    except:
        log.exception('Error writing to file in {}'.format(file_path))
        raise
    """,
    """
    def __parse_archive_args(self, archive_args):

        if not archive_args:
            return None

        archiving_args = copy.deepcopy(archive_args)

        if self.archive_path:
            archiving_args['archive_path'] = self.archive_path
        else:
            archiving_args['archive_path'] = os.path.expanduser(ARCHIVES_DEFAULT_PATH)

        return ArchivingTaskConfig.from_dict(archiving_args)
    """
]

human_rewritten_codes = [
    """
    def JC69(mu=1.0, alphabet="nuc", **kwargs):
        num_chars = len(alphabets[alphabet])
        W = np.ones((num_chars, num_chars))
        pi = np.ones(num_chars)
        
        gtr = GTR(alphabet=alphabet)
        gtr.assign_rates(mu=mu, pi=pi, W=W)
        
        return gtr

    """,
    """
    def loop(self, sequences=None, outputs=None, non_sequences=None, block=None, **kwargs):
        from loop import Loop
        return Loop(sequences, outputs, non_sequences, block, **kwargs)

    """,
    """
    def _logsum_expbig_minus_expsmall(big, small):
        with tf.name_scope("logsum_expbig_minus_expsmall"):
            return tf.math.log1p(-tf.exp(small - big)) + big

    """,
    """
    def __openlib(self):
    if self.__getattribute__('_libloaded'):
        return
    
    libpath_list = self.__get_libres()
    for p in libpath_list:
        try:
            libres = resource_filename(self._module_name, p)
            self.lib = self.ffi.dlopen(libres)
            return
        except:
            continue

    """,
    """
    def __coord_cqt_hz(n, fmin=None, bins_per_octave=12, **_kwargs):
        if fmin is None:
            fmin = core.note_to_hz('C1')

        # Drop by half a bin to center CQT bins vertically
        return core.cqt_frequencies(
            n + 1,
            fmin=fmin / 2.0**(0.5 / bins_per_octave),
            bins_per_octave=bins_per_octave
        )

    """,
    """
    def run_samtools_index(job, bam):
        work_dir = job.fileStore.getLocalTempDir()
        local_bam_path = os.path.join(work_dir, 'sample.bam')
        job.fileStore.readGlobalFile(bam, local_bam_path)
        
        # Call: index the bam
        parameters = ['index', local_bam_path]
        dockerCall(
            job=job,
            workDir=work_dir,
            parameters=parameters,
            tool='quay.io/ucsc_cgl/samtools:0.1.19--dd5ac549b95eb3e5d166a5e310417ef13651994e'
        )
        
        # Write to fileStore
        return job.fileStore.writeGlobalFile(local_bam_path + '.bai')

    """,
    """
    def signature(frame):
    if not frame:
        return None
    
    code = frame.f_code
    return (code.co_name, code.co_filename, code.co_firstlineno)
    
    """,
    """
    import matplotlib.pyplot as plt

    N = len(all_boundaries)  # Number of lists of boundaries
    if algo_ids is None:
        algo_ids = io.get_algo_ids(est_file)

    # Translate ids
    for i, algo_id in enumerate(algo_ids):
        algo_ids[i] = translate_ids[algo_id]
    algo_ids = ["GT"] + algo_ids

    figsize = (6, 4)
    plt.figure(1, figsize=figsize, dpi=120, facecolor='w', edgecolor='k')
    for i, boundaries in enumerate(all_boundaries):
        color = "b"
        if i == 0:
            color = "r"  # Example color for the first set of boundaries
    """,
    """
    def write_to_file(file_path, content, encoding=None):
    try:
        # Determine the file mode and content type based on encoding
        mode = 'wb' if encoding else 'w'
        if encoding:
            content = content.encode(encoding)
        
        with open(file_path, mode) as f:
            f.write(content)
    except Exception as e:
        log.exception('Error writing to file in {}'.format(file_path))
        raise

    """,
    """
    def __parse_archive_args(self, archive_args):
    if not archive_args:
        return None

    archiving_args = copy.deepcopy(archive_args)

    if self.archive_path:
        archiving_args['archive_path'] = self.archive_path
    else:
        archiving_args['archive_path'] = os.path.expanduser(ARCHIVES_DEFAULT_PATH)

    return ArchivingTaskConfig.from_dict(archiving_args)

    """
]

AI_codes = [
    """
    def start_hb(self, callback):
        self._hb_task = loopingcall.FixedIntervalLoopingCall(callback)
        self._hb_task.start(interval=HEARTBEAT_INTERVAL)

    def stop_hb(self):
        #Stop the heartbeating task.
        if self._hb_task:
            self._hb_task.stop()
            self._hb_task = None

    def register_signal_handler(self, signum, callback, *args):
        #Register a signal handler.

        #Raise ValueError if the signal number is invalid or uncatchable.
        
        if signum in _SIGCHLD_HANDLERS:
    """,
    """
    def summary_gradient_updates(grads, opt, lr):
        grad_updates = [tf.reduce_sum(tf.abs(grad)) for grad in grads]
        grad_updates_summary = [tf.summary.scalar(name, update) for name, update in zip(opt.name, grad_updates)]
        return grad_updates_summary


    def summary_gradients(grads):
        #get summary ops for the magnitude of gradients
        grads_summary = [tf.summary.scalar(name, tf.reduce_mean(tf.abs(grad)))
    """,

    """
    def get_variant_info(genes):
    variant_info = {}
    for gene in genes:
        variant_name = gene.split(":")[0]
        chromosome = gene.split(":")[1]
        start = gene.split(":")[2]
        end = gene.split(":")[3]
        variant_info[variant_name] = {"chromosome": chromosome, "start": start, "end": end}
    return variant_inf
    """,

    """
    def _ep_need_close(self):
        return self._ep_closed

    def _ep_need_close_set(self, value):
        #Set the peer's end of the session closed flag.
        self._ep_closed = value

    def _ep_need_close_clear(self):
        #Clear the peer's end of the session closed flag.
        self._ep_closed = False

    def _ep_need_close_toggle(self):
        #Toggle the peer's end of the session closed flag.
        self._ep_closed
    """,
    """
    def _ep_need_close(self):
        return self._ep_closed

    def _ep_need_close_set(self, value):
        # Set the peer's end of the session closed flag.
        self._ep_closed = value

    def _ep_need_close_clear(self):
        # Clear the peer's end of the session closed flag.
        self._ep_closed = False

    def _ep_need_close_toggle(self):
        # Toggle the peer's end of the session closed flag.
        self._ep_closed = not self._ep_closed

    """,
    """
    def _handle_execute_reply(self, msg):
        self.logger.debug("Received reply: %s [%s]" % (msg.code, reply_to_msg))

        if msg.code in ('EOK', 'EOP'):
            self._close_server()
        elif msg.code.startswith('E'):
            code = msg.code.split(' ', 1)[1]
            # code = 'ec.EOK'
            self.send_error("Code '%s' failed! Check server logs for details." % code)
        elif (msg.code in ('EINPROGRESS', 'ECONNRESET', 'ENOTCONN') or
    """,
    """
    def update_caseid(self, case_obj, family_id):
        new_case = {
            k: v for k, v in case_obj.items()
            if k not in ["id", "rev", "type", "status", "family_id"]
        }

        new_case["id"] = new_case["rev"]
        new_case["family_id"] = family_id

        try:
            self.collection.update_one(
                {

    """,
    """
    def getEvents(self):
        events = []
        start_time = time.time() - 30
        while time.time() - start_time < 30:
            try:
                response = self.skype.get_events()
                events.extend(response.get('events', []))
            except:
                time.sleep(1)
        return events

    def get_weather(self, location):
    """,
    """
    def receiver_blueprint_for(self, name):
        try:
            blueprint = next((bp for bp in self.providers.values() for rp in bp.receivers if self.name in rp), None)
        except StopIteration:
            raise NotImplementedError(
                f"Provider {name} does not implement receivers for messages nor status reports."
            )
        if blueprint is not None:
            return blueprint

    """,
    """
    if outdir is None:
            outdir = os.path.join(self.outdir, 'minimal_export')
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        if analytes is None:
            analytes = self.analytes
        if samples is None:
            samples = self.samples
        if subset == 'All_Analyses':
            subset = self.analyses
    """
]

AI_rewritten_codes = [
    """
    def start_hb(self, callback):
        self._hb_task = loopingcall.FixedIntervalLoopingCall(callback)
        self._hb_task.start(interval=HEARTBEAT_INTERVAL)

    def stop_hb(self):
        # Stop the heartbeating task.
        if self._hb_task:
            self._hb_task.stop()
            self._hb_task = None

    def register_signal_handler(self, signum, callback, *args):
        # Register a signal handler.

        # Raise ValueError if the signal number is invalid or uncatchable.
        if signum in _SIGCHLD_HANDLERS:
            # Handle the signal registration logic here
            pass

    """,

    """
    def summary_gradient_updates(grads, opt, lr):
        grad_updates = [tf.reduce_sum(tf.abs(grad)) for grad in grads]
        grad_updates_summary = [tf.summary.scalar(f"{opt.name}_grad_update_{i}", update) for i, update in enumerate(grad_updates)]
        return grad_updates_summary

    def summary_gradients(grads):
        #Get summary ops for the magnitude of gradients
        grads_summary = [tf.summary.scalar(f"gradients_{i}", tf.reduce_mean(tf.abs(grad))) for i, grad in enumerate(grads)]
        return grads_summary

    """,
    """
    def get_variant_info(genes):
    variant_info = {}
    for gene in genes:
        variant_name, chromosome, start, end = gene.split(":")
        variant_info[variant_name] = {"chromosome": chromosome, "start": start, "end": end}
    return variant_info

    """,
    """
    def _ep_need_close(self):
        return self._ep_closed

    def _ep_need_close_set(self, value):
        # Set the peer's end of the session closed flag.
        self._ep_closed = value

    def _ep_need_close_clear(self):
        # Clear the peer's end of the session closed flag.
        self._ep_closed = False

    def _ep_need_close_toggle(self):
        # Toggle the peer's end of the session closed flag.
        self._ep_closed = not self._ep_closed

    """,
    """
    def _ep_need_close(self):
        return self._ep_closed

    def _ep_need_close_set(self, value):
        # Set the peer's end of the session closed flag.
        self._ep_closed = value

    def _ep_need_close_clear(self):
        # Clear the peer's end of the session closed flag.
        self._ep_closed = False

    def _ep_need_close_toggle(self):
        # Toggle the peer's end of the session closed flag.
        self._ep_closed = not self._ep_closed

    """,
    """
    def _handle_execute_reply(self, msg):
    self.logger.debug("Received reply: %s [%s]" % (msg.code, reply_to_msg))

    if msg.code in ('EOK', 'EOP'):
        self._close_server()
    elif msg.code.startswith('E'):
        code = msg.code.split(' ', 1)[1]
        self.send_error("Code '%s' failed! Check server logs for details." % code)
    elif msg.code in ('EINPROGRESS', 'ECONNRESET', 'ENOTCONN'):
        # Handle specific cases for these error codes
        pass

    """,
    """
    def update_caseid(self, case_obj, family_id):
        new_case = {
            k: v for k, v in case_obj.items()
            if k not in ["id", "rev", "type", "status", "family_id"]
        }

        new_case["id"] = case_obj["rev"]
        new_case["family_id"] = family_id

        try:
            self.collection.update_one(
                {"id": case_obj["id"]},
                {"$set": new_case}
            )
        except Exception as e:
            self.logger.error(f"Error updating case ID: {e}")
            raise

    """,
    """
    def getEvents(self):
        events = []
        start_time = time.time()

        while time.time() - start_time < 30:
            try:
                response = self.skype.get_events()
                events.extend(response.get('events', []))
            except Exception as e:
                self.logger.error(f"Error getting events: {e}")
                time.sleep(1)
        
        return events

    def get_weather(self, location):
        # Method implementation for getting weather information
        pass
    """,
    """
    def receiver_blueprint_for(self, name):
    try:
        blueprint = next(
            (bp for bp in self.providers.values() for rp in bp.receivers if self.name in rp),
            None
        )
    except StopIteration:
        raise NotImplementedError(
            f"Provider {name} does not implement receivers for messages nor status reports."
        )
    
    return blueprint

    """,
    """
    if outdir is None:
        outdir = os.path.join(self.outdir, 'minimal_export')

    if not os.path.exists(outdir):
        os.makedirs(outdir)

    if analytes is None:
        analytes = self.analytes

    if samples is None:
        samples = self.samples

    if subset == 'All_Analyses':
        subset = self.analyses

    """
]

def return_codes():
    return human_codes, human_rewritten_codes, AI_codes, AI_rewritten_codes
