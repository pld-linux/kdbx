Summary:	KDbxViewer - loading folder structure from Outlook Express 5.5 Directory
Summary(pl):	KDbxViewer - wczytywanie struktury folderów z katalogu Outlook Expressa 5.5
Name:		kdbx
Version:	0.7.1
Release:	1
License:	GPL
Group:		Applications/Files
Source0:	http://dl.sourceforge.net/ol2mbox/%{name}-%{version}.tar.gz
# Source0-md5:	933e285d151d1077edd0c92c98db7e1a
Patch0:		%{name}-kde.patch
URL:		http://sourceforge.net/projects/ol2mbox/
BuildRequires:	kdelibs-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDbxViewer is a program that can load the folder structure given in an
Outlook Express 5.5 Directory. You can extract these emails into
mailbox files.

%description -l pl
KDbxViewer to program wczytuj±cy sturkturê folderów z katalogu Outlook
Expressa 5.5. Listy mo¿na przekonwertowaæ do plików w standardowym
formacie skrzynek (mailbox).

%prep
%setup -q -n %{name}
%patch0 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure2_13 \
	--enable-mt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_applnkdir}/{Applications,Utilities}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/kdbx
%{_pixmapsdir}/locolor/*/apps/*.png
%{_applnkdir}/Utilities/*.desktop
