First, take a look at our `NuGet.config` file that lives in root of each project (and is "brought in" during `yarn` synchronization phase, as demonstrated yesterday):

https://github.com/pandell/web-pli/blob/master/packages/cli/sync/NuGet.config#L9-L14

1. (Oldest approach, strongly discouraged these days, kept only for "legacy reasons")
- Manually create `.nupkg` from `.nuspec` using `nuget`, then copy to `\\files\Systems_Admin\NuGetPackages` file share

2. Use Perforce + TeamCity (on its way out, 3rd party authors are publishing their assemblies via official Microsoft NuGet server more and more)
- Perforce (centralized source control provider) is much better at storing large binaries than Git, so we store 3rd party binaries alongside our `.nuspec` files here:
http://perforce.net.pandell.com:8088/shared/Tools/NuGetPackages/Source/?ac=83
- Example of `.nuspec` file:
http://perforce.net.pandell.com:8088/shared/Tools/NuGetPackages/Source/Advantage.Data.Provider/10.0.1.3/Advantage.Data.Provider.nuspec?ac=64&mu=296543
- MSBuild project file that is run on TeamCity (or locally to test as you add new packages):
http://perforce.net.pandell.com:8088/shared/Tools/NuGetPackages/Package.proj?ac=64&mu=362079
- When new package is added to Perforce, the following TeamCity target is then run manually:
https://build.pandell.com/project.html?projectId=P4NuGet&tab=projectOverview
- It collects all published `.nupkg` files as build artifacts, which makes them available via TeamCity NuGet server (see the above `NuGet.config` with TeamCity NuGet URL as one of the package providers)
- You can see latest published artifacts here:
https://build.pandell.com/viewLog.html?buildId=320148&tab=artifacts&buildTypeId=PandellNuGet_Package

milang [9:33 AM]
3. Create `.nupkg` in a project's build configuration, then capture it as build artifact (so that it is automatically shared)
- Pli, the "foundation class library" for all Pandell projects (it is only a matter of time before GregC starts asking you to start using Pli as well :wink2: ) is using this approach
- One solution (`.sln`) can have more than one package; in Pli every project/assembly (`.csproj`) (more-or-less) has its own `.nuspec` file, for example this is `Pandell.Common`:
https://github.com/pandell/Pli/blob/v6.2.0.1/src/Pandell.Common/Pandell.Common.nuspec
- Pli's NuGet packager is (unsurprisingly, I hope) called `3. Package`:
https://build.pandell.com/project.html?projectId=Pli&tab=projectOverview
- List of builds (a.k.a. Pli releases):
https://build.pandell.com/viewType.html?buildTypeId=Pli_Package&tab=buildTypeHistoryList&branch_Pli=__all_branches__
- And artifacts from the latest build:
https://build.pandell.com/viewLog.html?buildId=341961&tab=artifacts&buildTypeId=Pli_Package
