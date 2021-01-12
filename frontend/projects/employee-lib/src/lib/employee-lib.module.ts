import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { MatTableModule } from '@angular/material/table';

import { EmployeeTableComponent } from './components/employee-table/employee-table.component';



@NgModule({
  declarations: [EmployeeTableComponent],
  imports: [
    CommonModule,
    HttpClientModule,
    MatTableModule,
  ],
  exports: [EmployeeTableComponent]
})
export class EmployeeLibModule { }
