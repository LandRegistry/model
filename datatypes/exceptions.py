class NoSchemaException(Exception):
    def __init__(self):
        super(self.__class__, self).__init__("You have not defined a schema. You must overload the 'schema' method.")


class NoErrorDictionaryDefined(Exception):
    def __init__(self):
        super(self.__class__, self).__init__("You have not defined the method error_dictionary")


class FieldNameNotDefined(Exception):
    def __init__(self):
        super(self.__class__, self).__init__("You have not defined the method field_name")


class ErrorMessageNotDefined(Exception):
    def __init__(self):
        super(self.__class__, self).__init__("You have not defined the method error_message")


class DataDoesNotMatchSchemaException(Exception):
    def __init__(self, cause, field_name=None):
        super(self.__class__, self).__init__(cause.message + ', caused by ' + repr(cause))

        self.cause = cause

        self.field_errors = {e.path[0]: translate_error(e.error_message)
                             for e in self.cause.errors
                             if e.path is not [] and e.path is not None}

    def __repr__(self):
        return self.__class__.__name__ + ' errors:' + repr(self.field_errors) + ' caused by:' + repr(self.cause)

    def __str__(self):
        return self.__repr__()


def translate_error(message):
    # TODO: Translate voluptuous errors into generic useful form
    return message