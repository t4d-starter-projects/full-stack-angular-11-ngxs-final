import { Component, OnInit, Input } from '@angular/core';

import { Category } from '../../models/Category';

@Component({
  selector: 'lib-category-table',
  templateUrl: './category-table.component.html',
  styleUrls: ['./category-table.component.css']
})
export class CategoryTableComponent implements OnInit {

  public displayedColumns: string[] = ['categoryName', 'description'];

  @Input()
  public categories: Category[] = [];

  constructor() { }

  ngOnInit(): void {
  }

}
