import http

import rest_framework.permissions

import drfkwargs
import drfseriperm

import users.permissions
import users.models

User = users.models.User


class DefaultUserFFP(drfseriperm.FieldsForPermissions):
    include = [
        User.id.field.name,
        User.username.field.name,
        User.visible_username.field.name,
        User.avatar.field.name,
        User.date_joined.field.name,
    ]
    extra_kwargs = {
        User.date_joined.field.name: {drfkwargs.READ_ONLY: True},
    }


class DefaultUserUpdateExtendFFP(drfseriperm.FieldsForPermissions):
    extra_kwargs = {
        User.username.field.name: {drfkwargs.READ_ONLY: True},
        User.visible_username.field.name: {drfkwargs.READ_ONLY: True},
        User.avatar.field.name: {drfkwargs.READ_ONLY: True},
    }
    http_methods = [
        http.HTTPMethod.PUT,
        http.HTTPMethod.PATCH,
    ]


class DefaultUserPostExtendFFP(drfseriperm.FieldsForPermissions):
    include = [User.password.field.name]
    extra_kwargs = {
        User.password.field.name: {drfkwargs.WRITE_ONLY: True},
        User.username.field.name: {drfkwargs.READ_ONLY: False},
        User.visible_username.field.name: {drfkwargs.READ_ONLY: False},
        User.avatar.field.name: {drfkwargs.READ_ONLY: False},
    }
    http_methods = [http.HTTPMethod.POST]


class AccountOwnerFFP(DefaultUserPostExtendFFP):
    permissions = [users.permissions.IsAccountOwner]
    http_methods = [
        http.HTTPMethod.PUT,
        http.HTTPMethod.PATCH,
    ]


class StaffFFP(drfseriperm.FieldsForPermissions):
    include = [
        User.last_login.field.name,
        User.groups.field.name,
        User.user_permissions.field.name,
    ]
    permissions = [rest_framework.permissions.IsAdminUser]
    extra_kwargs = {
        User.visible_username.field.name: {drfkwargs.READ_ONLY: False},
        User.avatar.field.name: {drfkwargs.READ_ONLY: False},
        User.groups.field.name: {drfkwargs.READ_ONLY: True},
        User.user_permissions.field.name: {drfkwargs.READ_ONLY: True},
        User.last_login.field.name: {drfkwargs.READ_ONLY: True},
    }


class SuperuserFFP(drfseriperm.FieldsForPermissions):
    include = rest_framework.serializers.ALL_FIELDS
    permissions = [users.permissions.IsSuperuser]
    extra_kwargs = {
        User.date_joined.field.name: {drfkwargs.READ_ONLY: False},
        User.password.field.name: {drfkwargs.WRITE_ONLY: False},
        User.last_login.field.name: {drfkwargs.READ_ONLY: False},
        User.groups.field.name: {drfkwargs.READ_ONLY: False},
        User.user_permissions.field.name: {drfkwargs.READ_ONLY: False},
        User.last_login.field.name: {drfkwargs.READ_ONLY: False},
    }
