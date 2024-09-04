from result import Result
from typing import Optional

from gitviper.schema.organization import Organization


class OrgMixins:
    def get_organization(self, org: Optional[str] = None) -> Result[Organization, str]:
        return self.get("/orgs/{org}", Organization, org=org)
