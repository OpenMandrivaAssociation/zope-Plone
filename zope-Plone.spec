%define Product     Plone
%define name        zope-%{Product}
%define version     3.0.4
%define release     %mkrel 3
%define zope_minver 2.10.5

%define zope_home      %{_prefix}/lib/zope
%define software_home  %{zope_home}/lib/python

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    A user friendly and powerful open source Content Management System
License:    GPL
Group:      System/Servers
URL:        http://plone.org/
Source:     http://plone.googlecode.com/files/%{Product}-%{version}.tar.gz
Requires:   python2.4-wicked
Requires:   python2.4-imaging
Requires:   python2.4-elementtree
Requires:   zope >= %{zope_minver}
Requires:   zope-ATContentTypes >= 1.2.3
Requires:   zope-ATReferenceBrowserWidget >= 2.0.1
Requires:   zope-AdvancedQuery >= 2.2
Requires:   zope-Archetypes >= 1.5.4
Requires:   zope-CMF >= 2.1.0
Requires:   zope-CMFDiffTool >= 0.3.5
Requires:   zope-CMFDynamicViewFTI >= 3.0.1
Requires:   zope-CMFEditions >= 1.1.4
Requires:   zope-CMFFormController >= 2.1.1
Requires:   zope-CMFPlacefulWorkflow >= 1.2.1
Requires:   zope-CMFQuickInstallerTool >= 2.0.4
Requires:   zope-CMFTestCase >= 0.9.6
Requires:   zope-ExtendedPathIndex >= 2.4
Requires:   zope-ExternalEditor >= 0.9.3
Requires:   zope-GroupUserFolder >= 3.55
Requires:   zope-NuPlone >= 0.9.3
Requires:   zope-PasswordResetTool >= 1.0
Requires:   zope-PlacelessTranslationService >= 1.4.6
Requires:   zope-PloneLanguageTool >= 2.0.1
Requires:   zope-PlonePAS >= 3.1
Requires:   zope-PloneTestCase >= 0.9.6
Requires:   zope-PloneTranslations >= 3.0.9
Requires:   zope-PluggableAuthService >= 1.5.2
Requires:   zope-PluginRegistry >= 1.1.2
Requires:   zope-ResourceRegistries >= 1.4.1
Requires:   zope-SecureMailHost >= 1.1
Requires:   zope-ZopeVersionControl >= 0.3.4
Requires:   zope-kupu >= 1.4.6
Requires:   zope-statusmessages >= 3.0.3
Obsoletes:  zope-CMFPlone
Provides:   zope-CMFPlone
Suggests:   zope-PloneErrorReporting >= 1.0
Suggests:   zope-CacheFu
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Plone is powerful and flexible. It is ideal as an intranet and
extranet server, as a document publishing system, a portal server and
as a groupware tool for collaboration between separately located
entities.

Plone is easy to use. The Plone Team includes usability experts who
have made Plone easy and attractive for content managers to add,
update, and maintain content.

Plone is international. The Plone interface has been translated into
over 40 languages, and tools exist for managing multilingual content.

Plone is standard. Plone carefully follows standards for usability and
accessibility. Plone pages are compliant with US Section 508, and the
W3C's AA rating for accessibility, in addition to using best-practice
web standards like XHTML and CSS.

Plone is Open Source. Plone is licensed under the GNU General Public
License, the same license Linux uses. This gives you the right to use
Plone without a license fee, and to improve upon the product.

Plone is supported. There are close to a hundred developers in the
Plone Development Team around the world, and a multitude of companies
specializing in Plone development and support.

Plone is extensible. There are many add-on products for Plone that add
new features and content types. In addition, Plone can be scripted
using web standard solutions and Open Source languages.

Plone is technology neutral. Plone can interoperate with most
relational database systems, open source and commercial, and runs on a
vast array of platforms, including Linux, Windows, Mac OS X, Solaris
and BSD.

Plone is protected. The nonprofit Plone Foundation was formed in 2004
to promote the use of Plone around the world and protect the Plone IP
and trademarks.

Plone is built using Zope, an object oriented application server. The
language that drives Zope and Plone is Python - the agile language
preferred by Google, NASA, Industrial Light and Magic and many
others. Why? Because Python offers unprecedented programmer
productivity.

%prep
%setup -q -n %{Product}-%{version}

%build
# nothing to do here

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
# copy only CMFPlone folder
%{__cp} -a Products/CMFPlone %{buildroot}%{software_home}/Products/
%{__cp} -a lib/python/archetypes \
    lib/python/five \
    lib/python/kss \
    lib/python/plone \
    %{buildroot}%{software_home}

%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(-,root,root)
%doc INSTALL.txt README.txt RELEASENOTES.txt
%{software_home}/Products/*
%{software_home}/plone
%{software_home}/kss
%{software_home}/archetypes
%{software_home}/five

