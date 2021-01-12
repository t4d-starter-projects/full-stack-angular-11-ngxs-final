import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { MatTableModule } from '@angular/material/table';

import { CategoryTableComponent } from './components/category-table/category-table.component';



@NgModule({
  declarations: [CategoryTableComponent],
  imports: [
    CommonModule,
    HttpClientModule,
    MatTableModule,
  ],
  exports: [CategoryTableComponent]
})
export class CategoryLibModule { }
