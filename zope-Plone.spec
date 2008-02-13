%define Product     Plone
%define name        zope-%{Product}
%define version     3.0.5
%define release     %mkrel 2
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
Patch0:	    Plone-3.0.5-i18n.app.102.patch
BuildArch:  noarch
Requires:   python2.4-wicked
Requires:   python2.4-imaging
Requires:   python2.4-elementtree
Requires:   zope >= %{zope_minver}
Obsoletes:  zope-AdvancedQuery
Provides:   zope-AdvancedQuery
Obsoletes:  zope-Archetypes
Provides:   zope-Archetypes
Obsoletes:  zope-ATContentTypes
Provides:   zope-ATContentTypes
Obsoletes:  zope-ATReferenceBrowserWidget
Provides:   zope-ATReferenceBrowserWidget
Obsoletes:  zope-CMF
Provides:   zope-CMF
Obsoletes:  zope-CMFDiffTool
Provides:   zope-CMFDiffTool
Obsoletes:  zope-CMFDynamicViewFTI
Provides:   zope-CMFDynamicViewFTI
Obsoletes:  zope-CMFEditions
Provides:   zope-CMFEditions
Obsoletes:  zope-CMFFormController
Provides:   zope-CMFFormController
Obsoletes:  zope-CMFPlacefulWorkflow
Provides:   zope-CMFPlacefulWorkflow
Obsoletes:  zope-CMFQuickInstallerTool
Provides:   zope-CMFQuickInstallerTool
Obsoletes:  zope-CMFTestCase
Provides:   zope-CMFTestCase
Obsoletes:  zope-ExtendedPathIndex
Provides:   zope-ExtendedPathIndex
Obsoletes:  zope-CMFTestCase
Provides:   zope-CMFTestCase
Obsoletes:  zope-ExternalEditor
Provides:   zope-ExternalEditor
Obsoletes:  zope-GenericSetup
Provides:   zope-GenericSetup
Obsoletes:  zope-GroupUserFolder
Provides:   zope-GroupUserFolder
Obsoletes:  zope-kupu
Provides:   zope-kupu
Obsoletes:  zope-NuPlone
Provides:   zope-NuPlone
Obsoletes:  zope-PasswordResetTool
Provides:   zope-PasswordResetTool
Obsoletes:  zope-PlacelessTranslationService
Provides:   zope-PlacelessTranslationService
Obsoletes:  zope-PloneBase
Provides:   zope-PloneBase
Obsoletes:  zope-PloneLanguageTool
Provides:   zope-PloneLanguageTool
Obsoletes:  zope-PlonePAS
Provides:   zope-PlonePAS
Obsoletes:  zope-PloneTestCase
Provides:   zope-PloneTestCase
Obsoletes:  zope-PloneTranslations
Provides:   zope-PloneTranslations
Obsoletes:  zope-PluggableAuthService
Provides:   zope-PluggableAuthService
Obsoletes:  zope-PluginRegistry
Provides:   zope-PluginRegistry
Obsoletes:  zope-ResourceRegistries
Provides:   zope-ResourceRegistries
Obsoletes:  zope-SecureMailHost
Provides:   zope-SecureMailHost
Obsoletes:  zope-statusmessages
Provides:   zope-statusmessages
Obsoletes:  zope-ZopeVersionControl
Provides:   zope-ZopeVersionControl
Obsoletes:  zope-CMFPlone
Provides:   zope-CMFPlone
Suggests:   zope-PloneErrorReporting >= 1.0
Suggests:   zope-CacheFu
BuildRequires: gettext
%if %{mdkversion} <= 200800
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
%endif

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
%patch0 -p1

find . -type d \( -name CVS -o -name .svn \) -print0 | xargs -0 rm -rf
find . -type f \( -name .cvsignore -name '*~' \) -print0 | xargs -0 rm -f

%build
# nothing to do here

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products


# convert .po files
for file_po in `find ./ -name "*.po" -type f`; do
    file_dir=${file_po#./}
    file_dir=${file_dir%/*}
    file_mo=${file_po##*/}
    file_mo=${file_mo%.po}.mo
    echo "Converting $file_po to $file_dir/$file_mo..."
    msgfmt -o $file_dir/$file_mo $file_po --no-hash || :
done

%{__cp} -a Products/* %{buildroot}%{software_home}/Products/
%{__cp} -a lib/python/* %{buildroot}%{software_home}

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
%{software_home}/archetypes
%{software_home}/five
%{software_home}/kss
%{software_home}/plone
%{software_home}/wicked
