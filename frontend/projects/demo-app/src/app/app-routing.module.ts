import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LoggedInGuardService } from '@t4d-wnow/user-lib';
import { AllowedRolesGuardService } from '@t4d-wnow/user-lib';

import { HomeComponent } from './pages/home/home.component';
import { ProfileComponent } from './pages/profile/profile.component';
import { LogoutComponent } from './pages/logout/logout.component';

const routes: Routes = [
  { path: '', pathMatch: 'full', component: HomeComponent },
  {
    path: 'profile',
    component: ProfileComponent,
    canActivate: [LoggedInGuardService, AllowedRolesGuardService],
    data: {
      roles: ['user'],
      title: 'Profile Page',
    },
  },
  {
    path: 'categories',
    loadChildren: () =>
      import('./category-tool/category-tool.module')
        .then(m => m.CategoryToolModule),
  },
  {
    path: 'employees',
    loadChildren: () =>
      import('./employee-tool/employee-tool.module')
        .then(m => m.EmployeeToolModule),
  },
  { path: 'login', pathMatch: 'full', redirectTo: '/' },
  { path: 'notauthorized', pathMatch: 'full', redirectTo: '/' },
  { path: 'logout', pathMatch: 'full', component: LogoutComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
