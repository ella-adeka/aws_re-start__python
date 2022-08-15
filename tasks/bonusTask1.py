# ### Bonus 1:

# Building

# | BuildingID | int |
# | --- | --- |
# | ComplexID | int |
# | BuildingName | varchar(100) |
# | Address | varchar(100) |

# Apartments

# | AptID | int |
# | --- | --- |
# | UnitNumber | varchar(10) |
# | BuildingID | int |

# Requests

# | RequestID | int |
# | --- | --- |
# | Status | varchar(100) |
# | AptID | int |
# | Description | varchar(100) |

# Complexes

# | ComplexID | int |
# | --- | --- |
# | ComplexName | varchar(100) |

# Tenants

# | TenantID | int |
# | --- | --- |
# | TenantName | varchar(100) |

# AptTenants

# | TenantID | int |
# | --- | --- |
# | AptID | int |

# Given the above SQL tables, write a query that:

# 1. Gets a list of tenants who are renting more than one apartment.
# 2. Write a SQL query to get a list of all buildings and the number of open requests (Requests in which status equals 'Open').
