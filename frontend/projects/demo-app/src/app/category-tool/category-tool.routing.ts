import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { CategoriesComponent } from './pages/categories/categories.component';

import { CategoriesResolverService } from '@t4d-wnow/category-lib';
import { LoggedInGuardService, AllowedRolesGuardService } from '@t4d-wnow/user-lib';

const routes: Routes = [
  {
    path: '',
    component: CategoriesComponent,
    resolve: {
      categories: CategoriesResolverService,
    },
    canActivate: [LoggedInGuardService, AllowedRolesGuardService],
    data: {
      roles: ['user'],
      title: 'Categories Page',
    },
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class CategoryToolRoutingModule {}