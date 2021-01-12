import { Component, OnInit, Input } from '@angular/core';
import { Employee } from '../../models/Employee';

@Component({
  selector: 'lib-employee-table',
  templateUrl: './employee-table.component.html',
  styleUrls: ['./employee-table.component.css']
})
export class EmployeeTableComponent implements OnInit {

  public displayedColumns: string[] = [
    'username', 'firstName', 'lastName', 'title'];

  @Input()
  public employees: Employee[] = [];

  constructor() { }

  ngOnInit(): void {
  }

}
