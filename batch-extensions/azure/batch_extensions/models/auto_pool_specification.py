# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AutoPoolSpecification(Model):
    """Specifies characteristics for a temporary 'auto pool'. The Batch service
    will create this auto pool when the job is submitted.

    :param auto_pool_id_prefix: A prefix to be added to the unique identifier
     when a pool is automatically created. The Batch service assigns each auto
     pool a unique identifier on creation. To distinguish between pools created
     for different purposes, you can specify this element to add a prefix to
     the id that is assigned. The prefix can be up to 20 characters long.
    :type auto_pool_id_prefix: str
    :param pool_lifetime_option: The minimum lifetime of created auto pools,
     and how multiple jobs on a schedule are assigned to pools. When the pool
     lifetime scope is jobSchedule level, the Batch service keeps track of the
     last autopool created for the job schedule, and deletes that pool when the
     job schedule completes. Batch will also delete this pool if the user
     updates the auto pool specification in a way that changes this lifetime.
     Possible values include: 'jobSchedule', 'job'
    :type pool_lifetime_option: str or :class:`PoolLifetimeOption
     <azure.batch.models.PoolLifetimeOption>`
    :param keep_alive: Whether to keep an auto pool alive after its lifetime
     expires. If false, the Batch service deletes the pool once its lifetime
     (as determined by the poolLifetimeOption setting) expires; that is, when
     the job or job schedule completes. If true, the Batch service does not
     delete the pool automatically. It is up to the user to delete auto pools
     created with this option.
    :type keep_alive: bool
    :param pool: The pool specification for the auto pool.
    :type pool: :class:`PoolSpecification
     <azure.batch.models.PoolSpecification>`
    """

    _validation = {
        'pool_lifetime_option': {'required': True},
    }

    _attribute_map = {
        'auto_pool_id_prefix': {'key': 'autoPoolIdPrefix', 'type': 'str'},
        'pool_lifetime_option': {'key': 'poolLifetimeOption', 'type': 'PoolLifetimeOption'},
        'keep_alive': {'key': 'keepAlive', 'type': 'bool'},
        'pool': {'key': 'pool', 'type': 'ExtendedPoolSpecification'},
    }

    def __init__(self, pool_lifetime_option, auto_pool_id_prefix=None, keep_alive=None, pool=None):
        self.auto_pool_id_prefix = auto_pool_id_prefix
        self.pool_lifetime_option = pool_lifetime_option
        self.keep_alive = keep_alive
        self.pool = pool