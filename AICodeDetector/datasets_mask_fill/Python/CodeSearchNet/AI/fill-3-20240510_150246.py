def send html message.attach content backend EMAIL connection subject text True False html message.attach files message EmailMultiAlternatives message.cc alternative message in-reply-to message_id
        error 'backend.email.send', "EmailMultiAlternatives: Could not send email" unless fail ?
      end

      raise Errors::Send, 'errors: backend.email.send', "Error sending: #{message.body}" unless message.body["subject"].blank?
      true
    end

    def mass mail dryrun bcc def send bcc if files