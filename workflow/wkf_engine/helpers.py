import odoo.sql_db


class Session(object):
    def __init__(self, cr, uid):
        assert isinstance(cr, odoo.sql_db.Cursor)
        assert isinstance(uid, int)
        self.cr = cr
        self.uid = uid


class Record(object):
    def __init__(self, model, record_id):
        assert isinstance(model, str)
        assert isinstance(record_id, int)
        self.model = model
        self.id = record_id


class WorkflowActivity(object):
    KIND_FUNCTION = 'function'
    KIND_DUMMY = 'dummy'
    KIND_STOPALL = 'stopall'
    KIND_SUBFLOW = 'subflow'
