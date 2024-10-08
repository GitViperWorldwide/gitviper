# generated by datamodel-codegen:
#   filename:  team_update.json
#   timestamp: 2024-09-04T03:47:27+00:00

from __future__ import annotations

from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional


class Privacy(Enum):
    secret = "secret"
    closed = "closed"


class NotificationSetting(Enum):
    notifications_enabled = "notifications_enabled"
    notifications_disabled = "notifications_disabled"


class Permission(Enum):
    pull = "pull"
    push = "push"
    admin = "admin"


class TeamUpdate(BaseModel):
    name: Optional[str] = Field(None, description="The name of the team.")
    description: Optional[str] = Field(None, description="The description of the team.")
    privacy: Optional[Privacy] = Field(
        None,
        description="The level of privacy this team should have. Editing teams without specifying this parameter leaves `privacy` intact. When a team is nested, the `privacy` for parent teams cannot be `secret`. The options are:  \n**For a non-nested team:**  \n * `secret` - only visible to organization owners and members of this team.  \n * `closed` - visible to all members of this organization.  \n**For a parent or child team:**  \n * `closed` - visible to all members of this organization.",
    )
    notification_setting: Optional[NotificationSetting] = Field(
        None,
        description="The notification setting the team has chosen. Editing teams without specifying this parameter leaves `notification_setting` intact. The options are: \n * `notifications_enabled` - team members receive notifications when the team is @mentioned.  \n * `notifications_disabled` - no one receives notifications.",
    )
    permission: Optional[Permission] = Field(
        None,
        description="**Deprecated**. The permission that new repositories will be added to the team with when none is specified.",
    )
    parent_team_id: Optional[int] = Field(None, description="The ID of a team to set as the parent team.")
