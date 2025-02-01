# CEH

## Intro

    >>> Goal: Confidentiality, Integrity, Availability
    >>> Trade-off: Security - Functionality - Usability
    >>> Defense in depth: Multiple layers of security

    >>> Vulnerability: Weakness/flaw
    >>> Threat: Potentially violate the policy

    >>> Daisy Chaining/Pivoting: Using a successful attack to immediately launch another attack
    >>> Doxing: Publishing personally identifiable information (PII)

    >>> Non-repudiation: Inablity to deny that u did
    >>> Accountability: Responsible parties are held liable for actions the have taken
    >>> Authenticity: Proven fact that st is legitimate/real

    >>> NetSec Zoning allows an org manage different levels of netsec

## Control Access

    >>> MAC.Mandatory: Every object (resource) <-- a sensitivity label. Subject <-- a clearance level.
    >>? DAC.Discretionary: Identity-based (i.e. user-based/group-based) access control model
    >>> RBAC.Role-based: Permissions are granted to the role, not individual users
    >>> RuleBAC.Rule-based: Access is granted or denied based on whether or not a rule is met

## Cyber Kill Chain

    >>> Stages:
        - Reconnaissance
            Passive: Gathering in4 without interacting with the target 
                Footprinting: open source intelligence activity
            Active: Scanning

        - Weaponization: Identify or develop a malicious deliverable for conducting the attack
        - Delivery: Send the weaponized bundle to the victim
        - Exploitation: Executing code on the target system
        - Installation: Install malware on the target system
    
        - Command & Control: Establish a connection back to the command and control server
        - Actions on Objectives
