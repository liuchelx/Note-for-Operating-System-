Directory Server:
    contain a lookup service that provide mapping between network resources and thir network address
    repilication: the stored directory data can be copied and distributed across a number of physically distributed servers, but still appear as one
    OUs: organizational units

    DAP: Directory Access protocol
    DSP: Directory System Protocol
    DISP: Directory information shadowing PRotocol
    DOP:Directory Operational Bindings Managment Protocol
    LDAP: ligohtweght DAP

        AD: Active Directory, mircorsoft implementing, nost for windows
        OpenLDAP: Open source, work for all OS

Centralized management:
    a central service that provides instructions to all of the different parts of my IT infrastructure

    AAA: Directory services provide centralized authentication authorization and accounting, as AAA
    RBAC: role-based accesss contorl

LDAP:
    dn: Distinguished name
    CN: common name of the object
    OU: organizational unit, such as a group
    DC: domain component, #example.com is split into example
        -------------------------没看懂
        -------------------------什么是LDAP entry

     LDAP notation ： used for entries in directory services to describe attributes using values.

    bind operation
    three way to authenticate:  
        anoymous
        simple
        SASL: simple authentication and security layer
    Kerberos: a network authentication protocol used to suthenticate user indentity, secure the transfer

AD(Aactive Directory):
    ------------------整体有点问题，什么是domain，这个domain感觉跟DNS里面的domain不太一样,这个domain是一个工作组？ work group？
    ADAC: Active Directory Administrative Center
    Forest: the structure of the ADAC
    DC:domain controller
    read-write replicas
    ------------------domain controller 跟 domain Admin 有什么区别

    samAccountName: security acount  managment =sam

    all the active in ADAC is done by powershell, on the bottom of ADAC, we can check the code is running, then these code could be used to run a script

    group scope: 
        domain local
        global
        universal
        ------------没太懂这些是干嘛的，反倒是universal看懂了，其他两个具体是干嘛的，有什么区别？

Group policy
GPO: Group Policy Object
    contain computer configuration,user configuration or both
    when link the GPO, all the user or computer ALL will have that policy

    GPMC：group policy management console 
    WMI: Windows Management Instrumentation 

OpenLDAP:
    sudo apt-get install sladp ldap-utils # install the ldap
    sudo dkpg-reconfigure slapd #change the configure 

    PHPLDAPadmin: very similar to ADAC

     LDIF files:
        #some common cmmand:
        ldapadd: take the input of LDIF file and add the context of it
        ldapmodify
        ldapdelete
        ldapsearch