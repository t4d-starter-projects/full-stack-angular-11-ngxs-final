import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FlexLayoutModule } from '@angular/flex-layout';
import { MatCardModule } from '@angular/material/card';

import { CategoryLibModule } from '@t4d-wnow/category-lib';
import { CategoryToolRoutingModule } from './category-tool.routing';
import { CategoriesComponent } from './pages/categories/categories.component';


@NgModule({
  declarations: [CategoriesComponent],
  imports: [
    CommonModule,
    FlexLayoutModule,
    MatCardModule,
    CategoryLibModule,
    CategoryToolRoutingModule,
  ]
})
export class CategoryToolModule { }
