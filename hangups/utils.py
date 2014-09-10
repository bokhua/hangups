def get_conv_name(conv, truncate=False):
    """Return the readable name for a conversation.

    For one-to-one conversations, the name is the full name of the other user.
    For group conversations, the name is a comma-separated list of first names.

    If truncate is true, only show up to two names in a group conversation.
    """
    participants = sorted((user for user in conv.users if not user.is_self),
                          key=lambda user: user.id_)
    names = [user.first_name for user in participants]
    if len(participants) == 1:
        return participants[0].full_name
    elif truncate and len(participants) > 2:
        return ', '.join(names[:2] + ['+{}'.format(len(names) - 2)])
    else:
        return ', '.join(names)
