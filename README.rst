=======================
ansible-role-borgbackup
=======================

Ansible role to manage borgbackup

* License: Apache License, Version 2.0
* Documentation: https://ansible-role-borgbackup.readthedocs.org
* Source: https://git.openstack.org/cgit/openstack/ansible-role-borgbackup
* Bugs: https://bugs.launchpad.net/ansible-role-borgbackup

Description
-----------

BorgBackup (short: Borg) is a deduplicating backup program. Optionally, it
supports compression and authenticated encryption.

Requirements
------------

* pip3 to be installed if using borgbackup_install_method: (git|pip)

See `bindep.txt` for role dependencies.

Packages
~~~~~~~~

Package repository index files should be up to date before using this role, we
do not manage them.

Role Variables
--------------

Dependencies
------------

Example Playbook
----------------

.. code-block:: yaml

    - name: Install borgbackup
      hosts: foo
      roles:
        - ansible-role-borgbackup
