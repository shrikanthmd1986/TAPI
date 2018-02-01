# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.name_and_value import NameAndValue  # noqa: F401,E501
from tapi_server.models.path_objective_function import PathObjectiveFunction  # noqa: F401,E501
from tapi_server.models.path_optimization_constraint import PathOptimizationConstraint  # noqa: F401,E501
from tapi_server.models.path_service_end_point import PathServiceEndPoint  # noqa: F401,E501
from tapi_server.models.routing_constraint import RoutingConstraint  # noqa: F401,E501
from tapi_server.models.service_spec import ServiceSpec  # noqa: F401,E501
from tapi_server import util


class PathComputationService(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, uuid: str=None, name: List[NameAndValue]=None, path: List[str]=None, end_point: List[PathServiceEndPoint]=None, routing_constraint: RoutingConstraint=None, objective_function: PathObjectiveFunction=None, optimization_constraint: PathOptimizationConstraint=None):  # noqa: E501
        """PathComputationService - a model defined in Swagger

        :param uuid: The uuid of this PathComputationService.  # noqa: E501
        :type uuid: str
        :param name: The name of this PathComputationService.  # noqa: E501
        :type name: List[NameAndValue]
        :param path: The path of this PathComputationService.  # noqa: E501
        :type path: List[str]
        :param end_point: The end_point of this PathComputationService.  # noqa: E501
        :type end_point: List[PathServiceEndPoint]
        :param routing_constraint: The routing_constraint of this PathComputationService.  # noqa: E501
        :type routing_constraint: RoutingConstraint
        :param objective_function: The objective_function of this PathComputationService.  # noqa: E501
        :type objective_function: PathObjectiveFunction
        :param optimization_constraint: The optimization_constraint of this PathComputationService.  # noqa: E501
        :type optimization_constraint: PathOptimizationConstraint
        """
        self.swagger_types = {
            'uuid': str,
            'name': List[NameAndValue],
            'path': List[str],
            'end_point': List[PathServiceEndPoint],
            'routing_constraint': RoutingConstraint,
            'objective_function': PathObjectiveFunction,
            'optimization_constraint': PathOptimizationConstraint
        }

        self.attribute_map = {
            'uuid': 'uuid',
            'name': 'name',
            'path': 'path',
            'end_point': 'end-point',
            'routing_constraint': 'routing-constraint',
            'objective_function': 'objective-function',
            'optimization_constraint': 'optimization-constraint'
        }

        self._uuid = uuid
        self._name = name
        self._path = path
        self._end_point = end_point
        self._routing_constraint = routing_constraint
        self._objective_function = objective_function
        self._optimization_constraint = optimization_constraint

    @classmethod
    def from_dict(cls, dikt) -> 'PathComputationService':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The path-computation-service of this PathComputationService.  # noqa: E501
        :rtype: PathComputationService
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uuid(self) -> str:
        """Gets the uuid of this PathComputationService.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity. UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters. Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}  Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :return: The uuid of this PathComputationService.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        """Sets the uuid of this PathComputationService.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity. UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters. Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}  Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :param uuid: The uuid of this PathComputationService.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def name(self) -> List[NameAndValue]:
        """Gets the name of this PathComputationService.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this PathComputationService.
        :rtype: List[NameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name: List[NameAndValue]):
        """Sets the name of this PathComputationService.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this PathComputationService.
        :type name: List[NameAndValue]
        """

        self._name = name

    @property
    def path(self) -> List[str]:
        """Gets the path of this PathComputationService.


        :return: The path of this PathComputationService.
        :rtype: List[str]
        """
        return self._path

    @path.setter
    def path(self, path: List[str]):
        """Sets the path of this PathComputationService.


        :param path: The path of this PathComputationService.
        :type path: List[str]
        """

        self._path = path

    @property
    def end_point(self) -> List[PathServiceEndPoint]:
        """Gets the end_point of this PathComputationService.


        :return: The end_point of this PathComputationService.
        :rtype: List[PathServiceEndPoint]
        """
        return self._end_point

    @end_point.setter
    def end_point(self, end_point: List[PathServiceEndPoint]):
        """Sets the end_point of this PathComputationService.


        :param end_point: The end_point of this PathComputationService.
        :type end_point: List[PathServiceEndPoint]
        """

        self._end_point = end_point

    @property
    def routing_constraint(self) -> RoutingConstraint:
        """Gets the routing_constraint of this PathComputationService.


        :return: The routing_constraint of this PathComputationService.
        :rtype: RoutingConstraint
        """
        return self._routing_constraint

    @routing_constraint.setter
    def routing_constraint(self, routing_constraint: RoutingConstraint):
        """Sets the routing_constraint of this PathComputationService.


        :param routing_constraint: The routing_constraint of this PathComputationService.
        :type routing_constraint: RoutingConstraint
        """

        self._routing_constraint = routing_constraint

    @property
    def objective_function(self) -> PathObjectiveFunction:
        """Gets the objective_function of this PathComputationService.


        :return: The objective_function of this PathComputationService.
        :rtype: PathObjectiveFunction
        """
        return self._objective_function

    @objective_function.setter
    def objective_function(self, objective_function: PathObjectiveFunction):
        """Sets the objective_function of this PathComputationService.


        :param objective_function: The objective_function of this PathComputationService.
        :type objective_function: PathObjectiveFunction
        """

        self._objective_function = objective_function

    @property
    def optimization_constraint(self) -> PathOptimizationConstraint:
        """Gets the optimization_constraint of this PathComputationService.


        :return: The optimization_constraint of this PathComputationService.
        :rtype: PathOptimizationConstraint
        """
        return self._optimization_constraint

    @optimization_constraint.setter
    def optimization_constraint(self, optimization_constraint: PathOptimizationConstraint):
        """Sets the optimization_constraint of this PathComputationService.


        :param optimization_constraint: The optimization_constraint of this PathComputationService.
        :type optimization_constraint: PathOptimizationConstraint
        """

        self._optimization_constraint = optimization_constraint
