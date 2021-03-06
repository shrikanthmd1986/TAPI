# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.connectivity_constraint import ConnectivityConstraint  # noqa: F401,E501
from tapi_server.models.connectivity_service_end_point import ConnectivityServiceEndPoint  # noqa: F401,E501
from tapi_server.models.resilience_constraint import ResilienceConstraint  # noqa: F401,E501
from tapi_server.models.topology_constraint import TopologyConstraint  # noqa: F401,E501
from tapi_server import util


class CreateConnectivityServiceRPCInputSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, end_point: List[ConnectivityServiceEndPoint]=None, conn_constraint: ConnectivityConstraint=None, topo_constraint: TopologyConstraint=None, resilience_constraint: List[ResilienceConstraint]=None, state: str=None):  # noqa: E501
        """CreateConnectivityServiceRPCInputSchema - a model defined in Swagger

        :param end_point: The end_point of this CreateConnectivityServiceRPCInputSchema.  # noqa: E501
        :type end_point: List[ConnectivityServiceEndPoint]
        :param conn_constraint: The conn_constraint of this CreateConnectivityServiceRPCInputSchema.  # noqa: E501
        :type conn_constraint: ConnectivityConstraint
        :param topo_constraint: The topo_constraint of this CreateConnectivityServiceRPCInputSchema.  # noqa: E501
        :type topo_constraint: TopologyConstraint
        :param resilience_constraint: The resilience_constraint of this CreateConnectivityServiceRPCInputSchema.  # noqa: E501
        :type resilience_constraint: List[ResilienceConstraint]
        :param state: The state of this CreateConnectivityServiceRPCInputSchema.  # noqa: E501
        :type state: str
        """
        self.swagger_types = {
            'end_point': List[ConnectivityServiceEndPoint],
            'conn_constraint': ConnectivityConstraint,
            'topo_constraint': TopologyConstraint,
            'resilience_constraint': List[ResilienceConstraint],
            'state': str
        }

        self.attribute_map = {
            'end_point': 'end-point',
            'conn_constraint': 'conn-constraint',
            'topo_constraint': 'topo-constraint',
            'resilience_constraint': 'resilience-constraint',
            'state': 'state'
        }

        self._end_point = end_point
        self._conn_constraint = conn_constraint
        self._topo_constraint = topo_constraint
        self._resilience_constraint = resilience_constraint
        self._state = state

    @classmethod
    def from_dict(cls, dikt) -> 'CreateConnectivityServiceRPCInputSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The create-connectivity-serviceRPC_input_schema of this CreateConnectivityServiceRPCInputSchema.  # noqa: E501
        :rtype: CreateConnectivityServiceRPCInputSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def end_point(self) -> List[ConnectivityServiceEndPoint]:
        """Gets the end_point of this CreateConnectivityServiceRPCInputSchema.


        :return: The end_point of this CreateConnectivityServiceRPCInputSchema.
        :rtype: List[ConnectivityServiceEndPoint]
        """
        return self._end_point

    @end_point.setter
    def end_point(self, end_point: List[ConnectivityServiceEndPoint]):
        """Sets the end_point of this CreateConnectivityServiceRPCInputSchema.


        :param end_point: The end_point of this CreateConnectivityServiceRPCInputSchema.
        :type end_point: List[ConnectivityServiceEndPoint]
        """

        self._end_point = end_point

    @property
    def conn_constraint(self) -> ConnectivityConstraint:
        """Gets the conn_constraint of this CreateConnectivityServiceRPCInputSchema.


        :return: The conn_constraint of this CreateConnectivityServiceRPCInputSchema.
        :rtype: ConnectivityConstraint
        """
        return self._conn_constraint

    @conn_constraint.setter
    def conn_constraint(self, conn_constraint: ConnectivityConstraint):
        """Sets the conn_constraint of this CreateConnectivityServiceRPCInputSchema.


        :param conn_constraint: The conn_constraint of this CreateConnectivityServiceRPCInputSchema.
        :type conn_constraint: ConnectivityConstraint
        """

        self._conn_constraint = conn_constraint

    @property
    def topo_constraint(self) -> TopologyConstraint:
        """Gets the topo_constraint of this CreateConnectivityServiceRPCInputSchema.


        :return: The topo_constraint of this CreateConnectivityServiceRPCInputSchema.
        :rtype: TopologyConstraint
        """
        return self._topo_constraint

    @topo_constraint.setter
    def topo_constraint(self, topo_constraint: TopologyConstraint):
        """Sets the topo_constraint of this CreateConnectivityServiceRPCInputSchema.


        :param topo_constraint: The topo_constraint of this CreateConnectivityServiceRPCInputSchema.
        :type topo_constraint: TopologyConstraint
        """

        self._topo_constraint = topo_constraint

    @property
    def resilience_constraint(self) -> List[ResilienceConstraint]:
        """Gets the resilience_constraint of this CreateConnectivityServiceRPCInputSchema.


        :return: The resilience_constraint of this CreateConnectivityServiceRPCInputSchema.
        :rtype: List[ResilienceConstraint]
        """
        return self._resilience_constraint

    @resilience_constraint.setter
    def resilience_constraint(self, resilience_constraint: List[ResilienceConstraint]):
        """Sets the resilience_constraint of this CreateConnectivityServiceRPCInputSchema.


        :param resilience_constraint: The resilience_constraint of this CreateConnectivityServiceRPCInputSchema.
        :type resilience_constraint: List[ResilienceConstraint]
        """

        self._resilience_constraint = resilience_constraint

    @property
    def state(self) -> str:
        """Gets the state of this CreateConnectivityServiceRPCInputSchema.


        :return: The state of this CreateConnectivityServiceRPCInputSchema.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this CreateConnectivityServiceRPCInputSchema.


        :param state: The state of this CreateConnectivityServiceRPCInputSchema.
        :type state: str
        """

        self._state = state
