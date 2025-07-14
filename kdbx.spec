Summary:	KDbxViewer - loading folder structure from Outlook Express 5.5 directory
Summary(pl.UTF-8):	KDbxViewer - wczytywanie struktury folderów z katalogu Outlook Expressa 5.5
Name:		kdbx
Version:	0.7.1
Release:	5
License:	GPL
Group:		Applications/File
Source0:	http://dl.sourceforge.net/ol2mbox/%{name}-%{version}.tar.gz
# Source0-md5:	933e285d151d1077edd0c92c98db7e1a
Source1:        http://ep09.pld-linux.org/~djurban/kde/kde-common-admin.tar.bz2
# Source1-md5:	81e0b2f79ef76218381270960ac0f55f
Patch0:		%{name}-kde.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-desktop.patch
URL:		http://sourceforge.net/projects/ol2mbox/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDbxViewer is a program that can load the folder structure given in an
Outlook Express 5.5 directory. You can extract these emails into
mailbox files.

%description -l pl.UTF-8
KDbxViewer to program wczytujący strukturę folderów z katalogu Outlook
Expressa 5.5. Listy można przekonwertować do plików w standardowym
formacie skrzynek (mailbox).

%prep
%setup -q -n %{name} -a1
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%{__sed} -i -e "s,-ansi,,g" admin/*.*

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

export kde_appsdir="%{_desktopdir}"
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/kdbx
%{_iconsdir}/hicolor/*/apps/*.png
%{_desktopdir}/*.desktop
