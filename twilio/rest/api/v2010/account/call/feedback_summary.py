# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class FeedbackSummaryList(ListResource):
    """  """

    def __init__(self, version, account_sid):
        """
        Initialize the FeedbackSummaryList

        :param Version version: Version that contains the resource
        :param account_sid: The unique id of the Account responsible for creating this Call

        :returns: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryList
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryList
        """
        super(FeedbackSummaryList, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/Calls/FeedbackSummary.json'.format(**self._solution)

    def create(self, start_date, end_date, include_subaccounts=values.unset,
               status_callback=values.unset, status_callback_method=values.unset):
        """
        Create a new FeedbackSummaryInstance

        :param date start_date: The start_date
        :param date end_date: The end_date
        :param bool include_subaccounts: The include_subaccounts
        :param unicode status_callback: The status_callback
        :param unicode status_callback_method: The status_callback_method

        :returns: Newly created FeedbackSummaryInstance
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryInstance
        """
        data = values.of({
            'StartDate': serialize.iso8601_date(start_date),
            'EndDate': serialize.iso8601_date(end_date),
            'IncludeSubaccounts': include_subaccounts,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return FeedbackSummaryInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
        )

    def get(self, sid):
        """
        Constructs a FeedbackSummaryContext

        :param sid: The sid

        :returns: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryContext
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryContext
        """
        return FeedbackSummaryContext(
            self._version,
            account_sid=self._solution['account_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a FeedbackSummaryContext

        :param sid: The sid

        :returns: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryContext
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryContext
        """
        return FeedbackSummaryContext(
            self._version,
            account_sid=self._solution['account_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.FeedbackSummaryList>'


class FeedbackSummaryPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the FeedbackSummaryPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The unique id of the Account responsible for creating this Call

        :returns: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryPage
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryPage
        """
        super(FeedbackSummaryPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FeedbackSummaryInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryInstance
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryInstance
        """
        return FeedbackSummaryInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.FeedbackSummaryPage>'


class FeedbackSummaryContext(InstanceContext):
    """  """

    def __init__(self, version, account_sid, sid):
        """
        Initialize the FeedbackSummaryContext

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param sid: The sid

        :returns: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryContext
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryContext
        """
        super(FeedbackSummaryContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Calls/FeedbackSummary/{sid}.json'.format(**self._solution)

    def fetch(self):
        """
        Fetch a FeedbackSummaryInstance

        :returns: Fetched FeedbackSummaryInstance
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return FeedbackSummaryInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the FeedbackSummaryInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.FeedbackSummaryContext {}>'.format(context)


class FeedbackSummaryInstance(InstanceResource):
    """  """

    class Status(object):
        QUEUED = "queued"
        IN_PROGRESS = "in-progress"
        COMPLETED = "completed"
        FAILED = "failed"

    def __init__(self, version, payload, account_sid, sid=None):
        """
        Initialize the FeedbackSummaryInstance

        :returns: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryInstance
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryInstance
        """
        super(FeedbackSummaryInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'call_count': deserialize.integer(payload['call_count']),
            'call_feedback_count': deserialize.integer(payload['call_feedback_count']),
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'end_date': deserialize.iso8601_datetime(payload['end_date']),
            'include_subaccounts': payload['include_subaccounts'],
            'issues': payload['issues'],
            'quality_score_average': deserialize.decimal(payload['quality_score_average']),
            'quality_score_median': deserialize.decimal(payload['quality_score_median']),
            'quality_score_standard_deviation': deserialize.decimal(payload['quality_score_standard_deviation']),
            'sid': payload['sid'],
            'start_date': deserialize.iso8601_datetime(payload['start_date']),
            'status': payload['status'],
        }

        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: FeedbackSummaryContext for this FeedbackSummaryInstance
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryContext
        """
        if self._context is None:
            self._context = FeedbackSummaryContext(
                self._version,
                account_sid=self._solution['account_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def call_count(self):
        """
        :returns: The call_count
        :rtype: unicode
        """
        return self._properties['call_count']

    @property
    def call_feedback_count(self):
        """
        :returns: The call_feedback_count
        :rtype: unicode
        """
        return self._properties['call_feedback_count']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def end_date(self):
        """
        :returns: The end_date
        :rtype: datetime
        """
        return self._properties['end_date']

    @property
    def include_subaccounts(self):
        """
        :returns: The include_subaccounts
        :rtype: bool
        """
        return self._properties['include_subaccounts']

    @property
    def issues(self):
        """
        :returns: The issues
        :rtype: unicode
        """
        return self._properties['issues']

    @property
    def quality_score_average(self):
        """
        :returns: The quality_score_average
        :rtype: unicode
        """
        return self._properties['quality_score_average']

    @property
    def quality_score_median(self):
        """
        :returns: The quality_score_median
        :rtype: unicode
        """
        return self._properties['quality_score_median']

    @property
    def quality_score_standard_deviation(self):
        """
        :returns: The quality_score_standard_deviation
        :rtype: unicode
        """
        return self._properties['quality_score_standard_deviation']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def start_date(self):
        """
        :returns: The start_date
        :rtype: datetime
        """
        return self._properties['start_date']

    @property
    def status(self):
        """
        :returns: The status
        :rtype: FeedbackSummaryInstance.Status
        """
        return self._properties['status']

    def fetch(self):
        """
        Fetch a FeedbackSummaryInstance

        :returns: Fetched FeedbackSummaryInstance
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the FeedbackSummaryInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.FeedbackSummaryInstance {}>'.format(context)