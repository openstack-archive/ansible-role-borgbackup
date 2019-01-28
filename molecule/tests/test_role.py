# Copyright 2019 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


def test_backup_user(host):
    user = host.user('borgbackup')
    assert user.exists
    assert user.name == 'borgbackup'
    assert user.group == 'borgbackup'
    assert user.home == '/var/lib/borgbackup'

    f = host.file('/var/lib/borgbackup')
    assert f.exists
    assert f.is_directory
    assert f.user == 'borgbackup'
    assert f.group == 'borgbackup'
    assert f.mode == 0o755


def test_repos_directory(host):
    f = host.file('/var/lib/borgbackup/repos')
    assert f.exists
    assert f.is_directory
    assert f.user == 'borgbackup'
    assert f.group == 'borgbackup'
    assert f.mode == 0o755


def test_borgbackup_version(host):
    host.check_output('borg --version')
