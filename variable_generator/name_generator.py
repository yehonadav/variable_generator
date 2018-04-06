numbers = '1234567890'
letters = 'zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP'
valids = letters + '_' + numbers
invalids = '~`!@#$%^&*-=+|()[]{}<>,./\\?"\';:'
known_values = valids + invalids + " "
invalid_replacers = (
    '_tilda_',
    '_grave_accent_',
    '_exclamation_mark_',
    '_at_sign_',
    '_pound_',
    '_dollar_',
    '_percent_',
    '_circumflex_',
    '_ampersand_',
    '_asterisk_',
    '_hyphen_minus_',
    '_equal_',
    '_plus_',
    '_vertical_bar_',
    '_round_left_bracket_',
    '_round_right_bracket_',
    '_squar_left_bracket_',
    '_squar_right_bracket_',
    '_curly_left_bracket_',
    '_curly_right_bracket_',
    '_less_than_',
    '_more_than_',
    '_comma_',
    '_period_',
    '_slash_',
    '_backslash_',
    '_question_mark_',
    '_quotation_marks_',
    '_quotation_mark_',
    '_semicolon_',
    '_colon_')

replacer_map = []
for i in range(len(invalids)):
    replacer_map.append((invalids[i], invalid_replacers[i]))


def check_if_string_has_only_valid_values(string):
    """
    :type string: str
    :rtype: bool
    """
    return all(n in string for n in valids)


def check_for_string_unmapped_values(string):
    """
    :type string: str
    :rtype: str
    """
    unmapped_values = ""
    for s in string:
        if s not in known_values:
            unmapped_values += s
    return unmapped_values


def cut_off_string_edge_spaces(string):
    """
    :type string: str
    :rtype: str
    """
    while string.startswith(" "):
        string = string[1:]
    while string.endswith(" "):
        string = string[:-1]
    return string


def render_if_string_starts_with_a_number(string):
    """
    add "_" to the start if name starts with a digit
    :type string: str
    :rtype: str
    """
    if string[0].isdigit():
        string = "num" + string
    return string


def space_replacer(string):
    """
    :type string: str
    :rtype: str
    """
    string = string.replace(" ", "_")
    while "__" in string:
        string = string.replace("__", "_")
    return string


def render_string_known_invalids(string):
    """
    :type string: str
    :rtype: str
    """
    for replacer in replacer_map:
        if string[0] == replacer[0]:
            string = replacer[1][1:] + string[1:]
            break
    for replacer in replacer_map:
        if string[-1] == replacer[0]:
            string = string[:-1] + replacer[1][:-1]
            break
    for replacer in replacer_map:
        if replacer[0] in string:
            string = string.replace(replacer[0], replacer[1])
    return string


def render_string_unmapped_values(string, unmapped_values):
    """
    :type string: str
    :type unmapped_values: str
    :rtype: str
    """
    for s in unmapped_values:
        string = string.replace(s, "{}".format(ord(s)))
    return string


def generate_valid_variable_name(string: str):
    """
    :rtype: str
    """
    if len(string) == 0:
        raise ValueError('empty string')

    # check_if_string_has_only_valid_values
    string_has_only_valid_values = check_if_string_has_only_valid_values(string)

    # handle simple cases
    if string_has_only_valid_values is False:
        string = cut_off_string_edge_spaces(string)
        if len(string) == 0:
            raise ValueError('string cannot have only spaces')
        string_has_only_valid_values = check_if_string_has_only_valid_values(string)

    # handle exceptions
    if string_has_only_valid_values is False:
        # known exceptions
        string = render_string_known_invalids(string)

        #unknown exceptions
        unmapped_values = check_for_string_unmapped_values(string)
        if len(unmapped_values) > 0:
            string = render_string_unmapped_values(string, unmapped_values)

    # remove any cases where string has "__", "___", ..
    string = space_replacer(string)

    # add "num" if name starts with a number
    return render_if_string_starts_with_a_number(string)
