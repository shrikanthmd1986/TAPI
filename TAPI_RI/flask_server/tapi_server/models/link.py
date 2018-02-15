# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.admin_state_pac import AdminStatePac  # noqa: F401,E501
from tapi_server.models.capacity import Capacity  # noqa: F401,E501
from tapi_server.models.capacity_pac import CapacityPac  # noqa: F401,E501
from tapi_server.models.cost_characteristic import CostCharacteristic  # noqa: F401,E501
from tapi_server.models.latency_characteristic import LatencyCharacteristic  # noqa: F401,E501
from tapi_server.models.layer_protocol_transition_pac import LayerProtocolTransitionPac  # noqa: F401,E501
from tapi_server.models.name_and_value import NameAndValue  # noqa: F401,E501
from tapi_server.models.resilience_type import ResilienceType  # noqa: F401,E501
from tapi_server.models.resource_spec import ResourceSpec  # noqa: F401,E501
from tapi_server.models.risk_characteristic import RiskCharacteristic  # noqa: F401,E501
from tapi_server.models.risk_parameter_pac import RiskParameterPac  # noqa: F401,E501
from tapi_server.models.transfer_cost_pac import TransferCostPac  # noqa: F401,E501
from tapi_server.models.transfer_integrity_pac import TransferIntegrityPac  # noqa: F401,E501
from tapi_server.models.transfer_timing_pac import TransferTimingPac  # noqa: F401,E501
from tapi_server.models.validation_mechanism import ValidationMechanism  # noqa: F401,E501
from tapi_server.models.validation_pac import ValidationPac  # noqa: F401,E501
from tapi_server import util


class Link(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, uuid: str=None, name: List[NameAndValue]=None, administrative_state: str=None, operational_state: str=None, lifecycle_state: str=None, total_potential_capacity: Capacity=None, available_capacity: Capacity=None, cost_characteristic: List[CostCharacteristic]=None, error_characteristic: str=None, loss_characteristic: str=None, repeat_delivery_characteristic: str=None, delivery_order_characteristic: str=None, unavailable_time_characteristic: str=None, server_integrity_process_characteristic: str=None, latency_characteristic: List[LatencyCharacteristic]=None, risk_characteristic: List[RiskCharacteristic]=None, validation_mechanism: List[ValidationMechanism]=None, transitioned_layer_protocol_name: List[str]=None, node_edge_point: List[str]=None, layer_protocol_name: List[str]=None, direction: str=None, resilience_type: ResilienceType=None):  # noqa: E501
        """Link - a model defined in Swagger

        :param uuid: The uuid of this Link.  # noqa: E501
        :type uuid: str
        :param name: The name of this Link.  # noqa: E501
        :type name: List[NameAndValue]
        :param administrative_state: The administrative_state of this Link.  # noqa: E501
        :type administrative_state: str
        :param operational_state: The operational_state of this Link.  # noqa: E501
        :type operational_state: str
        :param lifecycle_state: The lifecycle_state of this Link.  # noqa: E501
        :type lifecycle_state: str
        :param total_potential_capacity: The total_potential_capacity of this Link.  # noqa: E501
        :type total_potential_capacity: Capacity
        :param available_capacity: The available_capacity of this Link.  # noqa: E501
        :type available_capacity: Capacity
        :param cost_characteristic: The cost_characteristic of this Link.  # noqa: E501
        :type cost_characteristic: List[CostCharacteristic]
        :param error_characteristic: The error_characteristic of this Link.  # noqa: E501
        :type error_characteristic: str
        :param loss_characteristic: The loss_characteristic of this Link.  # noqa: E501
        :type loss_characteristic: str
        :param repeat_delivery_characteristic: The repeat_delivery_characteristic of this Link.  # noqa: E501
        :type repeat_delivery_characteristic: str
        :param delivery_order_characteristic: The delivery_order_characteristic of this Link.  # noqa: E501
        :type delivery_order_characteristic: str
        :param unavailable_time_characteristic: The unavailable_time_characteristic of this Link.  # noqa: E501
        :type unavailable_time_characteristic: str
        :param server_integrity_process_characteristic: The server_integrity_process_characteristic of this Link.  # noqa: E501
        :type server_integrity_process_characteristic: str
        :param latency_characteristic: The latency_characteristic of this Link.  # noqa: E501
        :type latency_characteristic: List[LatencyCharacteristic]
        :param risk_characteristic: The risk_characteristic of this Link.  # noqa: E501
        :type risk_characteristic: List[RiskCharacteristic]
        :param validation_mechanism: The validation_mechanism of this Link.  # noqa: E501
        :type validation_mechanism: List[ValidationMechanism]
        :param transitioned_layer_protocol_name: The transitioned_layer_protocol_name of this Link.  # noqa: E501
        :type transitioned_layer_protocol_name: List[str]
        :param node_edge_point: The node_edge_point of this Link.  # noqa: E501
        :type node_edge_point: List[str]
        :param layer_protocol_name: The layer_protocol_name of this Link.  # noqa: E501
        :type layer_protocol_name: List[str]
        :param direction: The direction of this Link.  # noqa: E501
        :type direction: str
        :param resilience_type: The resilience_type of this Link.  # noqa: E501
        :type resilience_type: ResilienceType
        """
        self.swagger_types = {
            'uuid': str,
            'name': List[NameAndValue],
            'administrative_state': str,
            'operational_state': str,
            'lifecycle_state': str,
            'total_potential_capacity': Capacity,
            'available_capacity': Capacity,
            'cost_characteristic': List[CostCharacteristic],
            'error_characteristic': str,
            'loss_characteristic': str,
            'repeat_delivery_characteristic': str,
            'delivery_order_characteristic': str,
            'unavailable_time_characteristic': str,
            'server_integrity_process_characteristic': str,
            'latency_characteristic': List[LatencyCharacteristic],
            'risk_characteristic': List[RiskCharacteristic],
            'validation_mechanism': List[ValidationMechanism],
            'transitioned_layer_protocol_name': List[str],
            'node_edge_point': List[str],
            'layer_protocol_name': List[str],
            'direction': str,
            'resilience_type': ResilienceType
        }

        self.attribute_map = {
            'uuid': 'uuid',
            'name': 'name',
            'administrative_state': 'administrative-state',
            'operational_state': 'operational-state',
            'lifecycle_state': 'lifecycle-state',
            'total_potential_capacity': 'total-potential-capacity',
            'available_capacity': 'available-capacity',
            'cost_characteristic': 'cost-characteristic',
            'error_characteristic': 'error-characteristic',
            'loss_characteristic': 'loss-characteristic',
            'repeat_delivery_characteristic': 'repeat-delivery-characteristic',
            'delivery_order_characteristic': 'delivery-order-characteristic',
            'unavailable_time_characteristic': 'unavailable-time-characteristic',
            'server_integrity_process_characteristic': 'server-integrity-process-characteristic',
            'latency_characteristic': 'latency-characteristic',
            'risk_characteristic': 'risk-characteristic',
            'validation_mechanism': 'validation-mechanism',
            'transitioned_layer_protocol_name': 'transitioned-layer-protocol-name',
            'node_edge_point': 'node-edge-point',
            'layer_protocol_name': 'layer-protocol-name',
            'direction': 'direction',
            'resilience_type': 'resilience-type'
        }

        self._uuid = uuid
        self._name = name
        self._administrative_state = administrative_state
        self._operational_state = operational_state
        self._lifecycle_state = lifecycle_state
        self._total_potential_capacity = total_potential_capacity
        self._available_capacity = available_capacity
        self._cost_characteristic = cost_characteristic
        self._error_characteristic = error_characteristic
        self._loss_characteristic = loss_characteristic
        self._repeat_delivery_characteristic = repeat_delivery_characteristic
        self._delivery_order_characteristic = delivery_order_characteristic
        self._unavailable_time_characteristic = unavailable_time_characteristic
        self._server_integrity_process_characteristic = server_integrity_process_characteristic
        self._latency_characteristic = latency_characteristic
        self._risk_characteristic = risk_characteristic
        self._validation_mechanism = validation_mechanism
        self._transitioned_layer_protocol_name = transitioned_layer_protocol_name
        self._node_edge_point = node_edge_point
        self._layer_protocol_name = layer_protocol_name
        self._direction = direction
        self._resilience_type = resilience_type

    @classmethod
    def from_dict(cls, dikt) -> 'Link':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The link of this Link.  # noqa: E501
        :rtype: Link
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uuid(self) -> str:
        """Gets the uuid of this Link.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity. UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters. Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}  Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :return: The uuid of this Link.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        """Sets the uuid of this Link.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity. UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters. Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}  Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :param uuid: The uuid of this Link.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def name(self) -> List[NameAndValue]:
        """Gets the name of this Link.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this Link.
        :rtype: List[NameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name: List[NameAndValue]):
        """Sets the name of this Link.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this Link.
        :type name: List[NameAndValue]
        """

        self._name = name

    @property
    def administrative_state(self) -> str:
        """Gets the administrative_state of this Link.


        :return: The administrative_state of this Link.
        :rtype: str
        """
        return self._administrative_state

    @administrative_state.setter
    def administrative_state(self, administrative_state: str):
        """Sets the administrative_state of this Link.


        :param administrative_state: The administrative_state of this Link.
        :type administrative_state: str
        """
        allowed_values = ["LOCKED", "UNLOCKED"]  # noqa: E501
        if administrative_state not in allowed_values:
            raise ValueError(
                "Invalid value for `administrative_state` ({0}), must be one of {1}"
                .format(administrative_state, allowed_values)
            )

        self._administrative_state = administrative_state

    @property
    def operational_state(self) -> str:
        """Gets the operational_state of this Link.


        :return: The operational_state of this Link.
        :rtype: str
        """
        return self._operational_state

    @operational_state.setter
    def operational_state(self, operational_state: str):
        """Sets the operational_state of this Link.


        :param operational_state: The operational_state of this Link.
        :type operational_state: str
        """
        allowed_values = ["DISABLED", "ENABLED"]  # noqa: E501
        if operational_state not in allowed_values:
            raise ValueError(
                "Invalid value for `operational_state` ({0}), must be one of {1}"
                .format(operational_state, allowed_values)
            )

        self._operational_state = operational_state

    @property
    def lifecycle_state(self) -> str:
        """Gets the lifecycle_state of this Link.


        :return: The lifecycle_state of this Link.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state: str):
        """Sets the lifecycle_state of this Link.


        :param lifecycle_state: The lifecycle_state of this Link.
        :type lifecycle_state: str
        """
        allowed_values = ["PLANNED", "POTENTIAL_AVAILABLE", "POTENTIAL_BUSY", "INSTALLED", "PENDING_REMOVAL"]  # noqa: E501
        if lifecycle_state not in allowed_values:
            raise ValueError(
                "Invalid value for `lifecycle_state` ({0}), must be one of {1}"
                .format(lifecycle_state, allowed_values)
            )

        self._lifecycle_state = lifecycle_state

    @property
    def total_potential_capacity(self) -> Capacity:
        """Gets the total_potential_capacity of this Link.

        An optimistic view of the capacity of the TopologicalEntity assuming that any shared capacity is available to be taken.  # noqa: E501

        :return: The total_potential_capacity of this Link.
        :rtype: Capacity
        """
        return self._total_potential_capacity

    @total_potential_capacity.setter
    def total_potential_capacity(self, total_potential_capacity: Capacity):
        """Sets the total_potential_capacity of this Link.

        An optimistic view of the capacity of the TopologicalEntity assuming that any shared capacity is available to be taken.  # noqa: E501

        :param total_potential_capacity: The total_potential_capacity of this Link.
        :type total_potential_capacity: Capacity
        """

        self._total_potential_capacity = total_potential_capacity

    @property
    def available_capacity(self) -> Capacity:
        """Gets the available_capacity of this Link.

        Capacity available to be assigned.  # noqa: E501

        :return: The available_capacity of this Link.
        :rtype: Capacity
        """
        return self._available_capacity

    @available_capacity.setter
    def available_capacity(self, available_capacity: Capacity):
        """Sets the available_capacity of this Link.

        Capacity available to be assigned.  # noqa: E501

        :param available_capacity: The available_capacity of this Link.
        :type available_capacity: Capacity
        """

        self._available_capacity = available_capacity

    @property
    def cost_characteristic(self) -> List[CostCharacteristic]:
        """Gets the cost_characteristic of this Link.

        The list of costs where each cost relates to some aspect of the TopologicalEntity.  # noqa: E501

        :return: The cost_characteristic of this Link.
        :rtype: List[CostCharacteristic]
        """
        return self._cost_characteristic

    @cost_characteristic.setter
    def cost_characteristic(self, cost_characteristic: List[CostCharacteristic]):
        """Sets the cost_characteristic of this Link.

        The list of costs where each cost relates to some aspect of the TopologicalEntity.  # noqa: E501

        :param cost_characteristic: The cost_characteristic of this Link.
        :type cost_characteristic: List[CostCharacteristic]
        """

        self._cost_characteristic = cost_characteristic

    @property
    def error_characteristic(self) -> str:
        """Gets the error_characteristic of this Link.

        Describes the degree to which the signal propagated can be errored.  Applies to TDM systems as the errored signal will be propagated and not packet as errored packets will be discarded.  # noqa: E501

        :return: The error_characteristic of this Link.
        :rtype: str
        """
        return self._error_characteristic

    @error_characteristic.setter
    def error_characteristic(self, error_characteristic: str):
        """Sets the error_characteristic of this Link.

        Describes the degree to which the signal propagated can be errored.  Applies to TDM systems as the errored signal will be propagated and not packet as errored packets will be discarded.  # noqa: E501

        :param error_characteristic: The error_characteristic of this Link.
        :type error_characteristic: str
        """

        self._error_characteristic = error_characteristic

    @property
    def loss_characteristic(self) -> str:
        """Gets the loss_characteristic of this Link.

        Describes the acceptable characteristic of lost packets where loss may result from discard due to errors or overflow. Applies to packet systems and not TDM (as for TDM errored signals are propagated unless grossly errored and overflow/underflow turns into timing slips).  # noqa: E501

        :return: The loss_characteristic of this Link.
        :rtype: str
        """
        return self._loss_characteristic

    @loss_characteristic.setter
    def loss_characteristic(self, loss_characteristic: str):
        """Sets the loss_characteristic of this Link.

        Describes the acceptable characteristic of lost packets where loss may result from discard due to errors or overflow. Applies to packet systems and not TDM (as for TDM errored signals are propagated unless grossly errored and overflow/underflow turns into timing slips).  # noqa: E501

        :param loss_characteristic: The loss_characteristic of this Link.
        :type loss_characteristic: str
        """

        self._loss_characteristic = loss_characteristic

    @property
    def repeat_delivery_characteristic(self) -> str:
        """Gets the repeat_delivery_characteristic of this Link.

        Primarily applies to packet systems where a packet may be delivered more than once (in fault recovery for example).  It can also apply to TDM where several frames may be received twice due to switching in a system with a large differential propagation delay.  # noqa: E501

        :return: The repeat_delivery_characteristic of this Link.
        :rtype: str
        """
        return self._repeat_delivery_characteristic

    @repeat_delivery_characteristic.setter
    def repeat_delivery_characteristic(self, repeat_delivery_characteristic: str):
        """Sets the repeat_delivery_characteristic of this Link.

        Primarily applies to packet systems where a packet may be delivered more than once (in fault recovery for example).  It can also apply to TDM where several frames may be received twice due to switching in a system with a large differential propagation delay.  # noqa: E501

        :param repeat_delivery_characteristic: The repeat_delivery_characteristic of this Link.
        :type repeat_delivery_characteristic: str
        """

        self._repeat_delivery_characteristic = repeat_delivery_characteristic

    @property
    def delivery_order_characteristic(self) -> str:
        """Gets the delivery_order_characteristic of this Link.

        Describes the degree to which packets will be delivered out of sequence. Does not apply to TDM as the TDM protocols maintain strict order.  # noqa: E501

        :return: The delivery_order_characteristic of this Link.
        :rtype: str
        """
        return self._delivery_order_characteristic

    @delivery_order_characteristic.setter
    def delivery_order_characteristic(self, delivery_order_characteristic: str):
        """Sets the delivery_order_characteristic of this Link.

        Describes the degree to which packets will be delivered out of sequence. Does not apply to TDM as the TDM protocols maintain strict order.  # noqa: E501

        :param delivery_order_characteristic: The delivery_order_characteristic of this Link.
        :type delivery_order_characteristic: str
        """

        self._delivery_order_characteristic = delivery_order_characteristic

    @property
    def unavailable_time_characteristic(self) -> str:
        """Gets the unavailable_time_characteristic of this Link.

        Describes the duration for which there may be no valid signal propagated.  # noqa: E501

        :return: The unavailable_time_characteristic of this Link.
        :rtype: str
        """
        return self._unavailable_time_characteristic

    @unavailable_time_characteristic.setter
    def unavailable_time_characteristic(self, unavailable_time_characteristic: str):
        """Sets the unavailable_time_characteristic of this Link.

        Describes the duration for which there may be no valid signal propagated.  # noqa: E501

        :param unavailable_time_characteristic: The unavailable_time_characteristic of this Link.
        :type unavailable_time_characteristic: str
        """

        self._unavailable_time_characteristic = unavailable_time_characteristic

    @property
    def server_integrity_process_characteristic(self) -> str:
        """Gets the server_integrity_process_characteristic of this Link.

        Describes the effect of any server integrity enhancement process on the characteristics of the TopologicalEntity.  # noqa: E501

        :return: The server_integrity_process_characteristic of this Link.
        :rtype: str
        """
        return self._server_integrity_process_characteristic

    @server_integrity_process_characteristic.setter
    def server_integrity_process_characteristic(self, server_integrity_process_characteristic: str):
        """Sets the server_integrity_process_characteristic of this Link.

        Describes the effect of any server integrity enhancement process on the characteristics of the TopologicalEntity.  # noqa: E501

        :param server_integrity_process_characteristic: The server_integrity_process_characteristic of this Link.
        :type server_integrity_process_characteristic: str
        """

        self._server_integrity_process_characteristic = server_integrity_process_characteristic

    @property
    def latency_characteristic(self) -> List[LatencyCharacteristic]:
        """Gets the latency_characteristic of this Link.

        The effect on the latency of a queuing process. This only has significant effect for packet based systems and has a complex characteristic.  # noqa: E501

        :return: The latency_characteristic of this Link.
        :rtype: List[LatencyCharacteristic]
        """
        return self._latency_characteristic

    @latency_characteristic.setter
    def latency_characteristic(self, latency_characteristic: List[LatencyCharacteristic]):
        """Sets the latency_characteristic of this Link.

        The effect on the latency of a queuing process. This only has significant effect for packet based systems and has a complex characteristic.  # noqa: E501

        :param latency_characteristic: The latency_characteristic of this Link.
        :type latency_characteristic: List[LatencyCharacteristic]
        """

        self._latency_characteristic = latency_characteristic

    @property
    def risk_characteristic(self) -> List[RiskCharacteristic]:
        """Gets the risk_characteristic of this Link.

        A list of risk characteristics for consideration in an analysis of shared risk. Each element of the list represents a specific risk consideration.  # noqa: E501

        :return: The risk_characteristic of this Link.
        :rtype: List[RiskCharacteristic]
        """
        return self._risk_characteristic

    @risk_characteristic.setter
    def risk_characteristic(self, risk_characteristic: List[RiskCharacteristic]):
        """Sets the risk_characteristic of this Link.

        A list of risk characteristics for consideration in an analysis of shared risk. Each element of the list represents a specific risk consideration.  # noqa: E501

        :param risk_characteristic: The risk_characteristic of this Link.
        :type risk_characteristic: List[RiskCharacteristic]
        """

        self._risk_characteristic = risk_characteristic

    @property
    def validation_mechanism(self) -> List[ValidationMechanism]:
        """Gets the validation_mechanism of this Link.

        Provides details of the specific validation mechanism(s) used to confirm the presence of an intended topologicalEntity.  # noqa: E501

        :return: The validation_mechanism of this Link.
        :rtype: List[ValidationMechanism]
        """
        return self._validation_mechanism

    @validation_mechanism.setter
    def validation_mechanism(self, validation_mechanism: List[ValidationMechanism]):
        """Sets the validation_mechanism of this Link.

        Provides details of the specific validation mechanism(s) used to confirm the presence of an intended topologicalEntity.  # noqa: E501

        :param validation_mechanism: The validation_mechanism of this Link.
        :type validation_mechanism: List[ValidationMechanism]
        """

        self._validation_mechanism = validation_mechanism

    @property
    def transitioned_layer_protocol_name(self) -> List[str]:
        """Gets the transitioned_layer_protocol_name of this Link.


        :return: The transitioned_layer_protocol_name of this Link.
        :rtype: List[str]
        """
        return self._transitioned_layer_protocol_name

    @transitioned_layer_protocol_name.setter
    def transitioned_layer_protocol_name(self, transitioned_layer_protocol_name: List[str]):
        """Sets the transitioned_layer_protocol_name of this Link.


        :param transitioned_layer_protocol_name: The transitioned_layer_protocol_name of this Link.
        :type transitioned_layer_protocol_name: List[str]
        """

        self._transitioned_layer_protocol_name = transitioned_layer_protocol_name

    @property
    def node_edge_point(self) -> List[str]:
        """Gets the node_edge_point of this Link.


        :return: The node_edge_point of this Link.
        :rtype: List[str]
        """
        return self._node_edge_point

    @node_edge_point.setter
    def node_edge_point(self, node_edge_point: List[str]):
        """Sets the node_edge_point of this Link.


        :param node_edge_point: The node_edge_point of this Link.
        :type node_edge_point: List[str]
        """

        self._node_edge_point = node_edge_point

    @property
    def layer_protocol_name(self) -> List[str]:
        """Gets the layer_protocol_name of this Link.


        :return: The layer_protocol_name of this Link.
        :rtype: List[str]
        """
        return self._layer_protocol_name

    @layer_protocol_name.setter
    def layer_protocol_name(self, layer_protocol_name: List[str]):
        """Sets the layer_protocol_name of this Link.


        :param layer_protocol_name: The layer_protocol_name of this Link.
        :type layer_protocol_name: List[str]
        """
        allowed_values = ["OTSiA", "OCH", "OTU", "ODU", "ETH", "ETY"]  # noqa: E501
        if not set(layer_protocol_name).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `layer_protocol_name` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(layer_protocol_name) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._layer_protocol_name = layer_protocol_name

    @property
    def direction(self) -> str:
        """Gets the direction of this Link.

        The directionality of the Link.  Is applicable to simple Links where all LinkEnds are BIDIRECTIONAL (the Link will be BIDIRECTIONAL) or UNIDIRECTIONAL (the Link will be UNIDIRECTIONAL).  Is not present in more complex cases.  # noqa: E501

        :return: The direction of this Link.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction: str):
        """Sets the direction of this Link.

        The directionality of the Link.  Is applicable to simple Links where all LinkEnds are BIDIRECTIONAL (the Link will be BIDIRECTIONAL) or UNIDIRECTIONAL (the Link will be UNIDIRECTIONAL).  Is not present in more complex cases.  # noqa: E501

        :param direction: The direction of this Link.
        :type direction: str
        """
        allowed_values = ["BIDIRECTIONAL", "UNIDIRECTIONAL", "UNDEFINED_OR_UNKNOWN"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def resilience_type(self) -> ResilienceType:
        """Gets the resilience_type of this Link.


        :return: The resilience_type of this Link.
        :rtype: ResilienceType
        """
        return self._resilience_type

    @resilience_type.setter
    def resilience_type(self, resilience_type: ResilienceType):
        """Sets the resilience_type of this Link.


        :param resilience_type: The resilience_type of this Link.
        :type resilience_type: ResilienceType
        """

        self._resilience_type = resilience_type